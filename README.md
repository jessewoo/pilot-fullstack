# NAIRR Pilot Fullstack

A full-stack web application with a Wagtail CMS backend and SvelteKit frontend, containerized with Docker.

## Architecture

- **Backend**: Wagtail CMS (Django) - Headless CMS for content management
- **Frontend**: SvelteKit - Modern JavaScript framework for the user interface
- **Notebook**: Jupyter Lab - Data analysis and machine learning environment
- **Reverse Proxy**: Nginx - Routes requests between frontend and backend
- **Database**: SQLite (development)

## Project Structure

```
.
├── pilot-backend/          # Wagtail CMS backend
│   ├── mysite/            # Django project settings
│   ├── authentication/    # User authentication (login/logout/register)
│   ├── home/              # Home page models
│   ├── content/           # Content page models
│   ├── navigation/        # Navigation menu models
│   ├── footer/            # Footer models
│   ├── team/              # Team models
│   ├── faq/               # FAQ models
│   └── taxonomy/          # Taxonomy models
│
├── pilot-frontend/        # SvelteKit frontend
│   ├── src/
│   │   ├── lib/          # Components and API utilities
│   │   └── routes/       # SvelteKit routes
│   │       ├── login/    # Login page
│   │       ├── register/ # Registration page
│   │       └── logoff/   # Logout page
│   └── static/           # Static assets
│
├── pilot-notebook/        # Jupyter Lab environment
│   ├── Dockerfile         # Jupyter Lab Docker setup
│   └── *.ipynb           # Jupyter notebooks
│
├── nginx/                 # Nginx configuration
├── docker-compose.yml     # Production Docker setup
└── docker-compose.dev.yml # Development Docker setup
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Development Mode (with hot reload)

1. Clone the repository:
   ```bash
   git clone https://github.com/jessewoo/pilot-fullstack.git
   cd pilot-fullstack
   ```

2. Start the development environment:
   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```

3. Access the application:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/api/v2
   - Wagtail Admin: http://localhost:8000/admin
   - Jupyter Lab: http://localhost:8888

### Production Mode

1. Start the production environment:
   ```bash
   docker-compose up --build
   ```

2. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/v2
   - Wagtail Admin: http://localhost:8000/admin
   - Jupyter Lab: http://localhost:8888
   - Nginx Proxy: http://localhost:80

## Environment Variables

### Frontend

Create a `.env` file in `pilot-frontend/` with:

```env
PUBLIC_WAGTAIL_API_URL=http://localhost:8000/api/v2
PUBLIC_IMAGE_DOMAIN=http://localhost:8000
```

### Backend

Environment variables are set in `docker-compose.yml`:
- `DJANGO_SETTINGS_MODULE=mysite.settings.dev`
- `DATABASE_URL=sqlite:///db.sqlite3`

## API Endpoints

### Wagtail CMS API

- `GET /api/v2/pages/` - List all pages
- `GET /api/v2/pages/{id}/` - Get page by ID
- `GET /api/v2/page-by-slug/?slug={slug}` - Get page by slug
- `GET /api/v2/navigation_menus/` - List navigation menus

### Authentication API

- `POST /api/auth/login/` - User login (returns JWT access + refresh tokens)
- `POST /api/auth/logout/` - User logout (blacklists refresh token)
- `POST /api/auth/register/` - User registration (returns JWT tokens)
- `POST /api/auth/token/refresh/` - Refresh expired access token
- `GET /api/auth/user/` - Get current authenticated user details

## Development

### Backend Development

1. Access the backend container:
   ```bash
   docker exec -it wagtail-backend sh
   ```

2. Create Django superuser:
   ```bash
   python manage.py createsuperuser
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Frontend Development

The frontend uses SvelteKit with:
- Server-side rendering (SSR)
- File-based routing
- Hot module replacement (HMR) in dev mode

Key files:
- `src/lib/api/wagtail.js` - API client for Wagtail
- `src/routes/+layout.server.js` - Layout data (navigation menus)
- `src/routes/+page.server.js` - Home page data
- `src/routes/[slug]/+page.server.js` - Dynamic page data

### Jupyter Notebook Development

The notebook environment includes:
- Jupyter Lab interface
- Pre-installed data science libraries (numpy, pandas, matplotlib, seaborn, scikit-learn)
- Sample forest fire analysis notebook

Access Jupyter Lab at http://localhost:8888 (no password required in development).

To add more Python packages:
1. Update `pilot-notebook/Dockerfile` and rebuild:
   ```bash
   docker-compose -f docker-compose.dev.yml up --build notebook
   ```

### Viewing Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker logs -f svelte-frontend
docker logs -f wagtail-backend
docker logs -f jupyter-notebook
```

## Authentication

### JWT (JSON Web Token) Authentication

The application uses **JWT tokens with expiration** for secure authentication:

- **Token Types**:
  - **Access Token**: Short-lived (1 hour), used for API requests
  - **Refresh Token**: Long-lived (7 days), used to get new access tokens
- **Token Storage**:
  - Access tokens: `localStorage.accessToken`
  - Refresh tokens: `localStorage.refreshToken`
  - Blacklisted tokens: `token_blacklist_*` database tables

### Authentication Flow

1. **Login**: User submits credentials → Backend validates → Returns access + refresh tokens + user data
2. **Storage**: Frontend stores both tokens in `localStorage`
3. **API Requests**: Frontend includes access token in `Authorization: Bearer <token>` header
4. **Token Refresh**: When access token expires → Frontend uses refresh token to get new access token
5. **Logout**: Frontend calls logout endpoint → Backend blacklists refresh token → Frontend clears `localStorage`

### Security Features

✅ **Access tokens expire after 1 hour** - Limits exposure if token is stolen
✅ **Refresh tokens expire after 7 days** - Users must re-login weekly
✅ **Token rotation** - New refresh token issued on each refresh
✅ **Token blacklisting** - Old refresh tokens are invalidated on rotation
✅ **Automatic logout on token expiry** - Invalid tokens redirect to login
✅ **Proper server-side logout** - Refresh tokens blacklisted in database

### Token Refresh Mechanism

The frontend includes an automatic token refresh utility (`src/lib/utils/auth.js`) that:
- Detects expired access tokens (401 responses)
- Automatically refreshes using the refresh token
- Retries the original request with the new access token
- Redirects to login if refresh token is also expired

### API Authentication Endpoints

- `POST /api/auth/login/` - Login (returns access + refresh tokens)
- `POST /api/auth/logout/` - Logout (blacklists refresh token)
- `POST /api/auth/register/` - Register (returns access + refresh tokens)
- `POST /api/auth/token/refresh/` - Refresh access token
- `GET /api/auth/user/` - Get current authenticated user

### User Management

- Default admin account can be created via `python manage.py createsuperuser`
- Users can register via the frontend at `/register`
- User data stored in Django's `auth_user` table

### Migration from Old Token System

The old `rest_framework.authtoken` system has been replaced with JWT. To migrate:
1. Install new dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Users will need to re-login to get new JWT tokens

## CORS Configuration

The backend is configured to allow requests from:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (SvelteKit production)

Update `pilot-backend/mysite/settings/base.py` to add more origins.

## Troubleshooting

### Frontend can't connect to backend

- Ensure `PUBLIC_WAGTAIL_API_URL` uses `http://backend:8000/api/v2` in Docker
- Check CORS settings in `pilot-backend/mysite/settings/base.py`
- Verify all `.js` files making API calls are renamed to `.server.js`

### Images not loading

- Check that media files exist in `pilot-backend/media/`
- Ensure volume mounts are configured correctly in docker-compose
- Verify `PUBLIC_IMAGE_DOMAIN` is set correctly

### Hot reload not working

- Use `docker-compose.dev.yml` for development
- Ensure volume mounts are active
- Check that the frontend uses Vite dev server (port 5173)

## License

[Your License Here]
