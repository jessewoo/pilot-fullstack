from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
@permission_classes([AllowAny])
def login_view(request):
    """
    API endpoint for user login
    Accepts email/username and password, returns auth token
    """
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    # Try to authenticate with email or username
    user = None
    if email:
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(username=user_obj.username, password=password)
        except User.DoesNotExist:
            pass
    elif username:
        user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'success': True,
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        })
    else:
        return Response({
            'success': False,
            'message': 'Invalid credentials'
        }, status=400)


@api_view(['POST'])
def logout_view(request):
    """
    API endpoint for user logout
    Removes auth token and logs out user
    """
    if request.user.is_authenticated:
        # Delete the token
        try:
            request.user.auth_token.delete()
        except:
            pass

        logout(request)
        return Response({
            'success': True,
            'message': 'Logged out successfully'
        })

    return Response({
        'success': False,
        'message': 'Not authenticated'
    }, status=400)


@api_view(['GET'])
def current_user_view(request):
    """
    API endpoint to get current authenticated user details
    """
    if request.user.is_authenticated:
        return Response({
            'authenticated': True,
            'user': {
                'id': request.user.id,
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        })
    else:
        return Response({
            'authenticated': False
        }, status=401)
