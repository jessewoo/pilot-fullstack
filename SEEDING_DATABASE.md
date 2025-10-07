# Seeding Database with Sample Data

There are several ways to seed your database with sample data from `sample-db/db.sqlite3`.

## Option 1: Copy Entire Database (Simplest)

**⚠️ Warning: This will replace your current database**

```bash
# Backup current database (optional)
cp pilot-backend/db.sqlite3 pilot-backend/db.sqlite3.backup

# Copy sample database
cp sample-db/db.sqlite3 pilot-backend/db.sqlite3

# Restart containers
docker-compose -f docker-compose.dev.yml restart backend
```

## Option 2: Export/Import Specific Tables

Use the provided script to import only specific tables:

```bash
docker exec wagtail-backend sh -c "cd /app && ./seed_database.sh"
```

This will import:
- ✅ Pages (homepage, content pages)
- ✅ Images
- ✅ Navigation menus
- ✅ Footer data
- ✅ Team members (if any)
- ✅ FAQ items (if any)

## Option 3: Use Django Fixtures (Manual)

1. **Export data from sample database:**
```bash
# In sample-db directory with sample database
docker run --rm -v $(pwd)/sample-db:/data python:3.10 sh -c "
  pip install django wagtail &&
  cd /data &&
  python manage.py dumpdata --natural-foreign --natural-primary \
    wagtailcore.page home content navigation footer team faq taxonomy \
    > sample_fixture.json
"
```

2. **Load into current database:**
```bash
docker exec wagtail-backend python manage.py loaddata /path/to/sample_fixture.json
```

## Option 4: SQLite Direct Copy (Advanced)

Copy specific table data using SQLite:

```bash
# Attach sample database and copy tables
docker exec wagtail-backend sqlite3 db.sqlite3 "
ATTACH DATABASE '../sample-db/db.sqlite3' AS sample;

-- Copy pages
INSERT OR REPLACE INTO wagtailcore_page SELECT * FROM sample.wagtailcore_page;
INSERT OR REPLACE INTO home_homepage SELECT * FROM sample.home_homepage;

-- Copy navigation
INSERT OR REPLACE INTO navigation_navigationmenu SELECT * FROM sample.navigation_navigationmenu;
INSERT OR REPLACE INTO navigation_menuitem SELECT * FROM sample.navigation_menuitem;

-- Copy images
INSERT OR REPLACE INTO wagtailimages_image SELECT * FROM sample.wagtailimages_image;

DETACH DATABASE sample;
"
```

## What's in the Sample Database?

Check the sample database contents:

```bash
sqlite3 sample-db/db.sqlite3 "
SELECT COUNT(*) || ' pages' FROM wagtailcore_page
UNION ALL SELECT COUNT(*) || ' images' FROM wagtailimages_image
UNION ALL SELECT COUNT(*) || ' navigation menus' FROM navigation_navigationmenu;
"
```

Current sample data:
- 📄 10 pages
- 🖼️ 5 images
- 🧭 6 navigation menus

## Important Notes

⚠️ **Foreign Key Constraints**: Tables must be imported in the correct order due to foreign keys:
1. Locales, Collections, Sites
2. Images
3. Pages
4. Navigation, Footer, Team, etc.

⚠️ **Media Files**: If sample database references images, make sure to also copy:
```bash
cp -r sample-db/media/* pilot-backend/media/
```

⚠️ **User Accounts**: Sample database users won't work in new database. Create new superuser:
```bash
docker exec wagtail-backend python manage.py createsuperuser
```
