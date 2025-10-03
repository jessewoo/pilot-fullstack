# NAIRR Pilot Fullstack

A full-stack web application with a Wagtail CMS backend and SvelteKit frontend, containerized with Docker.

## Architecture

- **Backend**: Wagtail CMS (Django) - Headless CMS for content management
- **Frontend**: SvelteKit - Modern JavaScript framework for the user interface
- **Reverse Proxy**: Nginx - Routes requests between frontend and backend
- **Database**: SQLite (development)

## Project Structure

```
.
├── pilot-backend/          # Wagtail CMS backend
│   ├── mysite/            # Django project settings
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
│   └── static/           # Static assets
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

### Production Mode

1. Start the production environment:
   ```bash
   docker-compose up --build
   ```

2. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/api/v2
   - Wagtail Admin: http://localhost:8000/admin
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

The Wagtail API provides the following endpoints:

- `GET /api/v2/pages/` - List all pages
- `GET /api/v2/pages/{id}/` - Get page by ID
- `GET /api/v2/page-by-slug/?slug={slug}` - Get page by slug
- `GET /api/v2/navigation_menus/` - List navigation menus

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

### Viewing Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker logs -f svelte-frontend
docker logs -f wagtail-backend
```

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
