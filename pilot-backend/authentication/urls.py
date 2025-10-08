from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.login_view, name='api_login'),
    path('logout/', views.logout_view, name='api_logout'),
    path('register/', views.register_view, name='api_register'),
    path('user/', views.current_user_view, name='current_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
