#!/bin/bash
# Reset migrations script for fresh prototype database

echo "🔄 Resetting database and migrations..."

# Remove old database
rm -f db.sqlite3

# Create fresh migrations for all apps
echo "📝 Creating fresh migrations..."
python manage.py makemigrations home
python manage.py makemigrations search
python manage.py makemigrations navigation
python manage.py makemigrations content
python manage.py makemigrations footer
python manage.py makemigrations team
python manage.py makemigrations faq
python manage.py makemigrations taxonomy
python manage.py makemigrations authentication

# Run migrations
echo "⚡ Running migrations..."
python manage.py migrate

# Create superuser (optional - uncomment if needed)
# echo "👤 Creating superuser..."
# python manage.py createsuperuser --noinput --username admin --email admin@example.com || true

echo "✅ Database reset complete!"
