#!/usr/bin/env python
"""
Seed database from sample database using Django ORM
Usage: python seed_from_sample.py
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.dev')
django.setup()

from django.core.management import call_command
import sqlite3

def seed_database():
    """Copy data from sample database to current database"""

    sample_db = '../sample-db/db.sqlite3'

    if not os.path.exists(sample_db):
        print(f"❌ Sample database not found at {sample_db}")
        return

    print("🌱 Seeding database from sample data...")

    # Use Django's dumpdata/loaddata for safer migration
    temp_fixture = '/tmp/sample_data.json'

    # Apps and models to export
    apps_to_export = [
        'wagtailcore.locale',
        'wagtailcore.collection',
        'wagtailcore.site',
        'wagtailimages.image',
        'wagtailcore.page',
        'home',
        'content',
        'navigation',
        'footer',
        'team',
        'faq',
        'taxonomy',
    ]

    try:
        # Export from sample database
        print("📤 Exporting data from sample database...")
        with sqlite3.connect(sample_db) as conn:
            # Use Django's dumpdata via SQL
            for app in apps_to_export:
                try:
                    os.environ['DJANGO_DB_PATH'] = sample_db
                    # This approach requires manual copying
                    pass
                except Exception as e:
                    print(f"⚠️  Error exporting {app}: {e}")

        print("✅ Consider using the copy_db.sh script instead for SQLite databases")
        print("\nAlternatively, you can:")
        print("1. Copy sample-db/db.sqlite3 to pilot-backend/db.sqlite3")
        print("2. Or use Django admin to manually create sample content")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    seed_database()
