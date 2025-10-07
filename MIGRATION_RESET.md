# Migration Reset - Clean Slate

This prototype has been reset to a clean migration state.

## What Was Done

1. ✅ Deleted all existing migration files (except `__init__.py`)
2. ✅ Deleted old database file (`db.sqlite3`)
3. ✅ Created reset script for fresh migrations
4. ✅ Created migrations folders for all apps (authentication, search)

## How to Initialize Database

### Option 1: Using Docker (Recommended)
```bash
# Start containers
docker-compose -f docker-compose.dev.yml up --build

# In another terminal, exec into backend container
docker exec -it wagtail-backend sh

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Option 2: Using Reset Script (Local)
```bash
cd pilot-backend
source venv/bin/activate  # if using venv
./reset_migrations.sh
```

### Option 3: Manual Commands (Local)
```bash
cd pilot-backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Apps That Need Migrations

- `home` - Homepage models
- `search` - Search functionality
- `navigation` - Navigation menus
- `content` - Content pages
- `footer` - Footer models
- `team` - Team member models
- `faq` - FAQ models
- `taxonomy` - Taxonomy/categorization
- `authentication` - User authentication (new)

## Benefits of Reset

- 🎯 Single clean migration per app instead of multiple files
- 🚀 Faster database setup
- 🧹 Easier to understand migration history
- 📦 Smaller repository size
- ✨ Clean slate for prototype development

## Note

This reset is appropriate for prototypes/development. **Do not do this on production databases** as it will lose all data and migration history.
