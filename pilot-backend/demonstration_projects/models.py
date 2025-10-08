from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField


class DemonstrationProjectPage(Page):
    """A page model for demonstration projects with team members and project details"""

    PROJECT_TYPE_CHOICES = [
        ('research', 'Research'),
        ('education', 'Education'),
        ('infrastructure', 'Infrastructure'),
        ('application', 'Application'),
        ('other', 'Other'),
    ]

    # Project Information
    project_type = models.CharField(
        max_length=50,
        choices=PROJECT_TYPE_CHOICES,
        default='research',
        help_text="Type of demonstration project"
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text="Project subtitle or tagline"
    )

    project_intro = RichTextField(
        blank=True,
        help_text="Brief introduction or overview of the project"
    )

    # Project Lead
    project_lead_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Name of the project lead person"
    )

    project_lead_institution = models.CharField(
        max_length=255,
        blank=True,
        help_text="Institution of the project lead"
    )

    project_lead_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Photo of the project lead"
    )

    # Project Details
    project_info = RichTextField(
        blank=True,
        help_text="General project information and description"
    )

    more_information = RichTextField(
        blank=True,
        help_text="Additional detailed information about the project"
    )

    # Project Image
    project_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Main project image or banner"
    )

    # Admin panels
    content_panels = Page.content_panels + [
        FieldPanel('project_type'),
        FieldPanel('subtitle'),
        FieldPanel('project_intro'),
        FieldPanel('project_image'),

        MultiFieldPanel([
            FieldPanel('project_lead_name'),
            FieldPanel('project_lead_institution'),
            FieldPanel('project_lead_image'),
        ], heading="Project Lead"),

        MultiFieldPanel([
            FieldPanel('project_info'),
            FieldPanel('more_information'),
        ], heading="Project Details"),

        InlinePanel('team_members', label="Key Team Members"),
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
        APIField('project_intro'),
        APIField('project_lead_name'),
        APIField('project_lead_institution'),
        APIField('project_lead_image'),
        APIField('project_info'),
        APIField('more_information'),
        APIField('project_image'),
        APIField('team_members'),
        APIField('breadcrumbs', serializer=lambda self: self.get_breadcrumbs()),
    ]

    class Meta:
        verbose_name = "Demonstration Project"
        verbose_name_plural = "Demonstration Projects"


class DemonstrationProjectTeamMember(Orderable):
    """Key team members for a demonstration project"""

    project = ParentalKey(
        'DemonstrationProjectPage',
        related_name='team_members',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=255,
        help_text="Team member's full name"
    )

    institution = models.CharField(
        max_length=255,
        blank=True,
        help_text="Team member's institution or organization"
    )

    role = models.CharField(
        max_length=255,
        blank=True,
        help_text="Role or position in the project (e.g., 'Co-Investigator', 'Research Scientist')"
    )

    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Team member photo"
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('institution'),
        FieldPanel('role'),
        FieldPanel('photo'),
    ]

    api_fields = [
        APIField('name'),
        APIField('institution'),
        APIField('role'),
        APIField('photo'),
    ]

    def __str__(self):
        return f"{self.name} - {self.institution}" if self.institution else self.name

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
