# Authentication Security Upgrade - JWT Implementation

## Summary

Upgraded the authentication system from permanent tokens to **JWT (JSON Web Tokens) with expiration** for improved security.

## What Changed

### Backend Changes

1. **Added JWT Package** ([requirements.txt](pilot-backend/requirements.txt))
   - Added `djangorestframework-simplejwt>=5.3.0`

2. **Updated Settings** ([base.py](pilot-backend/mysite/settings/base.py))
   - Added `rest_framework_simplejwt` and `rest_framework_simplejwt.token_blacklist` to INSTALLED_APPS
   - Configured JWT settings with 1-hour access tokens and 7-day refresh tokens
   - Enabled token rotation and blacklisting

3. **Updated Authentication Views** ([authentication/views.py](pilot-backend/authentication/views.py))
   - `login_view`: Now returns `access` and `refresh` JWT tokens instead of permanent token
   - `logout_view`: Blacklists refresh token instead of deleting from database
   - `register_view`: Returns JWT tokens on registration

4. **Added Token Refresh Endpoint** ([authentication/urls.py](pilot-backend/authentication/urls.py))
   - `POST /api/auth/token/refresh/` - Get new access token using refresh token

### Frontend Changes

1. **Updated Login Component** ([Login.svelte](pilot-frontend/src/lib/components/Login.svelte))
   - Stores `accessToken` and `refreshToken` instead of `authToken`

2. **Updated Logoff Page** ([logoff/+page.svelte](pilot-frontend/src/routes/logoff/+page.svelte))
   - Uses `Bearer` token instead of `Token`
   - Sends refresh token to backend for blacklisting
   - Clears both access and refresh tokens from localStorage

3. **Created Auth Utility** ([lib/utils/auth.js](pilot-frontend/src/lib/utils/auth.js))
   - `refreshAccessToken()` - Automatically refresh expired access tokens
   - `authenticatedFetch()` - Make authenticated requests with auto-refresh
   - `isAuthenticated()` - Check if user is logged in
   - `getCurrentUser()` - Get current user from localStorage

## Security Improvements

| Feature | Old System | New System |
|---------|-----------|------------|
| **Token Expiration** | ❌ Never expires | ✅ 1 hour (access), 7 days (refresh) |
| **Token Type** | Permanent DB token | JWT with claims |
| **Token Refresh** | ❌ Not supported | ✅ Automatic refresh |
| **Token Revocation** | Delete from DB | ✅ Blacklist on logout |
| **Stolen Token Risk** | ⚠️ Valid forever | ✅ Limited to 1 hour |
| **Auto Logout** | ❌ Manual only | ✅ On token expiry |

## Installation Steps

### 1. Install Dependencies

```bash
cd pilot-backend
pip install djangorestframework-simplejwt>=5.3.0
```

Or using the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

This will create the token blacklist tables:
- `token_blacklist_outstandingtoken`
- `token_blacklist_blacklistedtoken`

### 3. Test the Changes

#### Test Login:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password123"}'
```

Expected response:
```json
{
  "success": true,
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "testuser",
    "email": "test@example.com"
  }
}
```

#### Test Token Refresh:
```bash
curl -X POST http://localhost:8000/api/auth/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "YOUR_REFRESH_TOKEN"}'
```

#### Test Authenticated Request:
```bash
curl -X GET http://localhost:8000/api/auth/user/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Token Lifecycle

```
Login/Register
    ↓
Receive access (1h) + refresh (7d) tokens
    ↓
Store in localStorage
    ↓
Make API requests with access token
    ↓
Access token expires after 1 hour
    ↓
Frontend detects 401 response
    ↓
Automatically refresh using refresh token
    ↓
Retry request with new access token
    ↓
If refresh token expired (7 days)
    ↓
Redirect to login page
```

## Migration Notes

### For Existing Users

Existing users will need to **re-login** after this upgrade because:
1. Old permanent tokens are incompatible with JWT
2. The authentication header format changed from `Token` to `Bearer`
3. Frontend now expects `access` and `refresh` tokens

### Database Cleanup (Optional)

The old `authtoken_token` table is no longer used but can remain for backward compatibility or be removed:

```bash
# Optional: Remove old token auth app from INSTALLED_APPS
# Then run:
python manage.py migrate authtoken zero
```

## Configuration

Token lifetimes can be adjusted in [base.py](pilot-backend/mysite/settings/base.py):

```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),    # Adjust access token lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),    # Adjust refresh token lifetime
    'ROTATE_REFRESH_TOKENS': True,                  # Generate new refresh on refresh
    'BLACKLIST_AFTER_ROTATION': True,               # Blacklist old refresh tokens
}
```

## Troubleshooting

### Issue: "Token is blacklisted" error
**Solution**: User tried to use an old refresh token. They need to login again.

### Issue: Access token expired
**Solution**: Frontend should automatically refresh. Check that `auth.js` utility is being used.

### Issue: 401 Unauthorized on every request
**Solution**: Verify Authorization header format is `Bearer <token>` not `Token <token>`

### Issue: Refresh token endpoint returns 401
**Solution**: Refresh token has expired (7 days). User must login again.

## Next Steps (Optional Improvements)

1. **Add HTTP-only cookies** - Store refresh tokens in HTTP-only cookies instead of localStorage
2. **Implement refresh token rotation** - Already enabled, but monitor blacklist table growth
3. **Add rate limiting** - Prevent brute force attacks on login endpoint
4. **Add 2FA** - Two-factor authentication for additional security
5. **Monitor token usage** - Track token refresh patterns for suspicious activity

## Support

For questions or issues, please check:
- [README.md](README.md) - General authentication documentation
- [Django REST Framework SimpleJWT docs](https://django-rest-framework-simplejwt.readthedocs.io/)
