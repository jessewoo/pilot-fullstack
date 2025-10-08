from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField


class SandboxProjectPage(Page):
    """A structured page model for sandbox/JupyterLab projects"""

    PROJECT_TYPE_CHOICES = [
        ('classroom', 'Classroom'),
        ('pilot', 'Pilot'),
        ('startup', 'Startup'),
    ]

    HOSTING_PLATFORM_CHOICES = [
        ('jetstream2', 'JetStream2'),
        ('huggingface', 'Hugging Face'),
        ('national_data_platform', 'National Data Platform'),
        ('other', 'Other'),
    ]

    # Main fields
    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPE_CHOICES,
        default='pilot',
        help_text="Type of project"
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text="Project subtitle or tagline"
    )

    principal_investigator = models.CharField(
        max_length=255,
        blank=True,
        help_text="Name of the principal investigator"
    )

    principal_investigator_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Principal investigator photo"
    )

    principal_investigator_url = models.URLField(
        blank=True,
        help_text="Principal investigator website or profile URL"
    )

    institution = models.CharField(
        max_length=255,
        blank=True,
        help_text="Institution or organization"
    )

    hosting_platform = models.CharField(
        max_length=50,
        choices=HOSTING_PLATFORM_CHOICES,
        blank=True,
        help_text="Platform where the project is hosted"
    )

    project_info = RichTextField(
        blank=True,
        help_text="General project information"
    )

    abstract = RichTextField(
        blank=True,
        help_text="Project abstract or summary"
    )

    references = RichTextField(
        blank=True,
        help_text="Project references and citations"
    )

    project_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Main project image"
    )

    github_repo_url = models.URLField(
        blank=True,
        help_text="GitHub repository URL"
    )

    # JupyterLab call to action
    jupyter_lab_url = models.URLField(
        blank=True,
        help_text="JupyterLab server URL"
    )

    jupyter_cta_text = models.CharField(
        max_length=100,
        default="Launch JupyterLab",
        help_text="Call to action button text"
    )

    # Admin panels
    content_panels = Page.content_panels + [
        FieldPanel('project_type'),
        FieldPanel('subtitle'),
        FieldPanel('principal_investigator'),
        FieldPanel('principal_investigator_image'),
        FieldPanel('principal_investigator_url'),
        FieldPanel('institution'),
        FieldPanel('hosting_platform'),
        FieldPanel('project_info'),
        FieldPanel('abstract'),
        FieldPanel('references'),
        FieldPanel('project_image'),
        FieldPanel('github_repo_url'),
        FieldPanel('jupyter_lab_url'),
        FieldPanel('jupyter_cta_text'),
    ]

    def get_breadcrumbs(self):
        """Return breadcrumb trail for this page"""
        breadcrumbs = []
        for ancestor in self.get_ancestors(inclusive=False).live().public():
            breadcrumbs.append({
                'title': ancestor.title,
                'url': ancestor.url,
                'slug': ancestor.slug,
            })
        # Add current page
        breadcrumbs.append({
            'title': self.title,
            'url': self.url,
            'slug': self.slug,
        })
        return breadcrumbs

    # API fields
    api_fields = [
        APIField('project_type'),
        APIField('subtitle'),
        APIField('principal_investigator'),
        APIField('principal_investigator_image'),
        APIField('principal_investigator_url'),
        APIField('institution'),
        APIField('hosting_platform'),
        APIField('project_info'),
        APIField('abstract'),
        APIField('references'),
        APIField('project_image'),
        APIField('github_repo_url'),
        APIField('jupyter_lab_url'),
        APIField('jupyter_cta_text'),
    ]
