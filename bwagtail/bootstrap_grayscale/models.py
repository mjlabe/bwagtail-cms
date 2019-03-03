from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import forms
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from django import forms

from bootstrap_common.models import *


class BootstrapGrayscaleMastheadBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    heading_image = ImageChooserBlock(required=False)
    subheading = blocks.RichTextBlock(required=False)
    background_image = ImageChooserBlock()
    button_text = blocks.CharBlock(required=False)
    button_link = blocks.PageChooserBlock(required=False)
    COLOR_CHOICES = (
        ('', 'Light'),
        ('dark', 'Dark'),
        ('theme', 'Theme')
    )
    background_theme = blocks.ChoiceBlock(choices=COLOR_CHOICES, required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if value['background_theme'] == 'dark':
            context['value']['btn_color'] = 'btn-light'
            context['value']['txt_color'] = '#f8f9fa'
        elif value['background_theme'] == 'theme':
            context['value']['btn_color'] = 'btn-primary'
            context['value']['txt_color'] = '#f8f9fa'
        else:
            context['value']['btn_color'] = 'btn-dark'
            context['value']['txt_color'] = '#050505'
        return context

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/grayscale_masthead_block.html'


class BootstrapGrayscaleAboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image_with_transparent_background = ImageChooserBlock(required=False)

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/grayscale_about_block.html'


class BootstrapGrayscaleFeaturedLargeRowBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading', blocks.CharBlock(required=False)),
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('image', ImageChooserBlock()),
        ('image_position', blocks.ChoiceBlock(choices=(('left', 'Left'), ('right', 'Right'))))
    ]))

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/featured/grayscale_featured_large_row_block.html'
        label = 'Featured Large Row'


class BootstrapGrayscaleFeaturedSmallRowBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading', blocks.CharBlock(required=False)),
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('image', ImageChooserBlock()),
        ('image_position', blocks.ChoiceBlock(choices=(('left', 'Left'), ('right', 'Right'))))
        ]))

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/featured/grayscale_featured_small_row_block.html'
        label = 'Featured Small Row'


class BootstrapGrayscaleFeaturedBlock(blocks.StructBlock):
    featured = blocks.StreamBlock([
        ('featured_row_large', BootstrapGrayscaleFeaturedLargeRowBlock()),
        ('featured_row', BootstrapGrayscaleFeaturedSmallRowBlock()),
    ])

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/featured/grayscale_featured_block.html'
        label = 'Featured'


class BootstrapGrayscaleSignupBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    background_image = ImageChooserBlock()

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/grayscale_signup_block.html'


class BootstrapGrayscaleContactBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    address = blocks.TextBlock(required=False)
    email = blocks.CharBlock()
    phone = blocks.CharBlock()
    SOCIAL_MEDIA = (
        ('fab fa-facebook-f', 'Facebook'),
        ('fab fa-instagram', 'Instagram'),
        ('fab fa-linkedin', 'LinkedIn'),
        ('fab fa-twitter', 'Twitter'),
        ('fab fa-pinterest', 'Pinterest'),
        ('fab fa-youtube', 'Youtube'),
        ('fab fa-github', 'GitHub'),
        ('fab fa-gitlab', 'GitLab'),
    )
    social_media = blocks.ListBlock(blocks.StructBlock([
        ('social_media', blocks.ChoiceBlock(SOCIAL_MEDIA)),
        ('social_link', blocks.URLBlock()),
    ], required=False))

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        address_query = value['address']

        # Remove all non-word characters (everything except numbers and letters)
        import re
        address_query = re.sub(r"[^\w\s]", '', address_query)

        # Replace all runs of whitespace with a single dash
        address_query = re.sub(r"\s+", '+', address_query)

        context['value']['address_query'] = address_query
        return context

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/grayscale_contact_block.html'


class BootstrapGrayscalePage(Page):
    body = StreamField([
        ('masthead', BootstrapGrayscaleMastheadBlock()),
        ('carousel', BootstrapCommonCarouselBlock()),
        ('about', BootstrapGrayscaleAboutBlock()),
        ('featured', BootstrapGrayscaleFeaturedBlock()),
        ('section', BootstrapCommonTextSectionBlock()),
        # ('signup', BootstrapGrayscaleSignupBlock()),      # Not functional on static site
        ('contact', BootstrapGrayscaleContactBlock()),
        ('grid', BootstrapCommonGridRowBlock()),
        ('pricing', BootstrapCommonPriceRowBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    seo_title = 'Bootstrap Grayscale Page'

#
# class Header(models.Model):
#     site_settings = ParentalKey('SiteSettings', on_delete=models.CASCADE, related_name='header')
#     site_name = models.CharField(max_length=50)
#     site_logo = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#     )
#     banner_colour = models.CharField(
#         max_length=6,
#         null=True,
#         blank=True,
#         help_text="Fill in a hex colour value"
#     )
#
#     panels = [
#         FieldPanel('site_name'),
#         ImageChooserPanel('site_logo'),
#         FieldPanel('banner_colour'),
#     ]

#
# class Footer(Orderable):
#     CONTACT_CHOICES = (
#         ('fas fa-phone', 'Phone'),
#         ('fas fa-envelope', 'Email'),
#         ('fab fa-facebook-f', 'Facebook'),
#         ('fa-instagram', 'Instagram'),
#         ('fab fa-linkedin', 'LinkedIn'),
#         ('fab fa-twitter', 'Twitter'),
#         ('fab fa-pinterest', 'Pinterest'),
#         ('fab fa-youtube', 'Youtube'),
#         ('fab fa-github', 'GitHub'),
#         ('fab fa-gitlab', 'GitLab'),
#     )
#
#     site_settings = ParentalKey('SiteSettings', on_delete=models.CASCADE, related_name='footer')
#     contact_type = models.CharField(choices=CONTACT_CHOICES, max_length=50)
#     contact_info = models.CharField(max_length=50)
#     info_prefix = models.CharField(max_length=10, editable=False)
#
#     def save(self, *args, **kwargs):
#         if self.contact_type == 'Phone':
#             self.info_prefix = 'tel:'
#         elif self.contact_type == 'Email':
#             self.info_prefix = 'mailto:'
#         else:
#             self.info_prefix = ''
#
#         super(Footer, self).save(*args, **kwargs)
#
#     panels = [
#         FieldPanel('contact_type'),
#         FieldPanel('contact_info'),
#     ]
#
#
# @register_setting
# class SiteSettings(BaseSetting, ClusterableModel):
#     site_name = models.CharField(max_length=50)
#     site_logo = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#     )
#     banner_color = models.CharField(
#         max_length=6,
#         null=True,
#         blank=True,
#         help_text="Fill in a hex colour value"
#     )
#     include_footer = models.BooleanField()
#
#     panels = [
#         FieldPanel('site_name'),
#         ImageChooserPanel('site_logo'),
#         FieldPanel('banner_color'),
#         FieldPanel('include_footer'),
#         InlinePanel('footer', label="Footer",
#                     help_text='Select your contact/social media type and enter the phone number, email, or URL')
#     ]
