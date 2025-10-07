#!/bin/bash
# Seed database from sample data

SAMPLE_DB="../sample-db/db.sqlite3"
CURRENT_DB="db.sqlite3"

echo "🌱 Seeding database from sample data..."

if [ ! -f "$SAMPLE_DB" ]; then
    echo "❌ Sample database not found at $SAMPLE_DB"
    exit 1
fi

# Tables to seed (in order due to foreign key constraints)
TABLES=(
    # Core Wagtail tables
    "wagtailcore_locale"
    "wagtailcore_collection"
    "wagtailcore_site"

    # Images
    "wagtailimages_image"
    "wagtailimages_rendition"

    # Pages (must come after images)
    "wagtailcore_page"
    "home_homepage"
    "home_htmlpage"
    "content_flexiblepage"
    "content_advancedflexiblepage"

    # Navigation
    "navigation_navigationmenu"
    "navigation_megamenu"
    "navigation_menuitem"
    "navigation_submenuitem"

    # Footer
    "footer_footer"
    "footer_footercolumn"
    "footer_footerlink"
    "footer_socialmedialink"

    # Team
    "team_department"
    "team_role"
    "team_teammember"
    "team_teammembersociallink"
    "team_expertisearea"

    # FAQ
    "faq_faqcategory"
    "faq_faqcollection"
    "faq_faqitem"
    "faq_faqcollectionitem"

    # Taxonomy
    "taxonomy_badge"
    "taxonomy_tag"
    "taxonomy_category"

    # Revisions (important for Wagtail)
    "wagtailcore_revision"
)

# Export and import each table
for table in "${TABLES[@]}"; do
    # Check if table has data in sample DB
    count=$(sqlite3 "$SAMPLE_DB" "SELECT COUNT(*) FROM $table" 2>/dev/null || echo "0")

    if [ "$count" -gt 0 ]; then
        echo "📦 Seeding $table ($count rows)..."

        # Export data from sample DB
        sqlite3 "$SAMPLE_DB" ".mode insert $table" "SELECT * FROM $table" > /tmp/seed_$table.sql 2>/dev/null

        # Import into current DB
        sqlite3 "$CURRENT_DB" < /tmp/seed_$table.sql 2>/dev/null

        # Clean up
        rm -f /tmp/seed_$table.sql
    else
        echo "⏭️  Skipping $table (no data)"
    fi
done

echo "✅ Database seeded successfully!"
echo ""
echo "📊 Summary:"
sqlite3 "$CURRENT_DB" "
SELECT COUNT(*) || ' pages' FROM wagtailcore_page
UNION ALL SELECT COUNT(*) || ' images' FROM wagtailimages_image
UNION ALL SELECT COUNT(*) || ' navigation menus' FROM navigation_navigationmenu
UNION ALL SELECT COUNT(*) || ' team members' FROM team_teammember
UNION ALL SELECT COUNT(*) || ' FAQ items' FROM faq_faqitem;
"
