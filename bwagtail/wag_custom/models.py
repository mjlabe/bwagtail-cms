import os

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel

from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import SettingMenuItem, register_setting

from django.db import models

from django.contrib.auth.models import Group
from wagtail.contrib.modeladmin.options import ModelAdmin

from django.apps import apps
from django.contrib.auth.models import Permission

from wagtail.core.models import Site, Page
from wagtailmenus.views import SiteSwitchForm
import wagtailmenus
from wagtail.images.edit_handlers import ImageChooserPanel

from django.contrib.auth.models import User


class Social(Orderable):
    CONTACT_CHOICES = (
        ('fas fa-phone', 'Phone'),
        ('fas fa-envelope', 'Email'),
        ('fab fa-facebook-f', 'Facebook'),
        ('fab fa-instagram', 'Instagram'),
        ('fab fa-linkedin', 'LinkedIn'),
        ('fab fa-twitter', 'Twitter'),
        ('fab fa-pinterest', 'Pinterest'),
        ('fab fa-youtube', 'Youtube'),
        ('fab fa-github', 'GitHub'),
        ('fab fa-gitlab', 'GitLab'),
    )

    site_settings = ParentalKey('SiteSettings', on_delete=models.CASCADE, related_name='social', null=True)
    social_type = models.CharField(choices=CONTACT_CHOICES, max_length=50)
    id_handle_contact = models.CharField(max_length=50, help_text='Link, phone number, or address')
    info_prefix = models.CharField(max_length=10, editable=False)
    social_url = models.CharField(max_length=50, editable=False)

    def save(self, *args, **kwargs):
        if self.social_type == 'Phone':
            self.info_prefix = 'tel:'
        elif self.social_type == 'Email':
            self.info_prefix = 'mailto:'
        else:
            self.info_prefix = ''

        self.social_url = 'www.{site}.com/{id_handle}'.format(site=self.get_social_type_display().lower(),
                                                              id_handle=self.id_handle_contact)

        super(Social, self).save(*args, **kwargs)

    panels = [
        FieldPanel('social_type'),
        FieldPanel('id_handle_contact'),
    ]

    def social_handle(self):
        if self.social_type != 'Phone' or 'Email':
            return self.id_handle_contact
        else:
            return ''


@register_setting
class SiteSettings(BaseSetting, ClusterableModel):
    site_name = models.CharField(max_length=50, blank=True, null=True)
    # TODO: make custom folder for site
    # TODO: validate file
    # site_logo = models.FileField(blank=True, null=True)
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    banner_color = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text="Fill in a hex colour value"
    )
    google_analytics_id = models.CharField(max_length=50, blank=True, null=True,
                                           help_text='Google Analytics Tracking ID')
    include_footer = models.BooleanField(null=True)

    panels = [
        FieldPanel('site_name'),
        ImageChooserPanel('site_logo'),
        FieldPanel('banner_color'),
        FieldPanel('google_analytics_id'),
        FieldPanel('include_footer'),
        InlinePanel('social', label="Social",
                    help_text='Select your contact/social media type and enter the phone number, email, or URL')
    ]
