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


class BootstrapBusinessCasualMastheadBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    subheading = blocks.RichTextBlock(required=False)
    background_image = ImageChooserBlock()
    masthead_image = ImageChooserBlock(help_text='Make sure this is a seamless image.')
    upper_text = blocks.TextBlock()
    lower_text = blocks.TextBlock()
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
        app_label = 'bootstrap_business_casual'
        template = 'bootstrap_business_casual/blocks/bootstrap_business_casual_masthead_block.html'


class BootstrapBusinessCasualCallBlock(blocks.StructBlock):
    heading_upper = blocks.CharBlock()
    heading_lower = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()

    class Meta:
        app_label = 'bootstrap_business_casual'
        template = 'bootstrap_business_casual/blocks/bootstrap_business_casual_call_block.html'
        label = 'Call To Action'


class BootstrapBusinessCasualAboutBlock(blocks.StructBlock):
    heading_upper = blocks.CharBlock()
    heading_lower = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        app_label = 'bootstrap_business_casual'
        template = 'bootstrap_business_casual/blocks/bootstrap_business_casual_about_block.html'
        label = 'About'


class BootstrapBusinessCasualProductsBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading_upper', blocks.CharBlock(required=False)),
        ('heading_lower', blocks.CharBlock(required=False)),
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('image', ImageChooserBlock(required=False)),
        # ('link1', blocks.PageChooserBlock(required=False))
        ]))

    class Meta:
        app_label = 'bootstrap_business_casual'
        template = 'bootstrap_business_casual/blocks/bootstrap_business_casual_products_block.html'
        label = 'Products'
# 
# class BootstrapBusinessCasualFeaturedLargeRowBlock(blocks.StructBlock):
#     item = blocks.ListBlock(blocks.StructBlock([
#         ('heading', blocks.CharBlock(required=False)),
#         ('paragraph', blocks.RichTextBlock(required=False)),
#         ('image', ImageChooserBlock()),
#         ('image_position', blocks.ChoiceBlock(choices=(('left', 'Left'), ('right', 'Right'))))
#     ]))
# 
#     class Meta:
#         app_label = 'bootstrap_business_casual'
#         template = 'bootstrap_business_casual/blocks/featured/business_casual_featured_large_row_block.html'
#         label = 'Featured Large Row'
# 
# 
# class BootstrapBusinessCasualFeaturedSmallRowBlock(blocks.StructBlock):
#     item = blocks.ListBlock(blocks.StructBlock([
#         ('heading', blocks.CharBlock(required=False)),
#         ('paragraph', blocks.RichTextBlock(required=False)),
#         ('image', ImageChooserBlock()),
#         ('image_position', blocks.ChoiceBlock(choices=(('left', 'Left'), ('right', 'Right'))))
#         ]))
# 
#     class Meta:
#         app_label = 'bootstrap_business_casual'
#         template = 'bootstrap_business_casual/blocks/featured/business_casual_featured_small_row_block.html'
#         label = 'Featured Small Row'
# 
# 
# class BootstrapBusinessCasualFeaturedBlock(blocks.StructBlock):
#     featured = blocks.StreamBlock([
#         ('featured_row_large', BootstrapBusinessCasualFeaturedLargeRowBlock()),
#         ('featured_row', BootstrapBusinessCasualFeaturedSmallRowBlock()),
#     ])
# 
#     class Meta:
#         app_label = 'bootstrap_business_casual'
#         template = 'bootstrap_business_casual/blocks/featured/business_casual_featured_block.html'
#         label = 'Featured'
# 
# 
# class BootstrapBusinessCasualSignupBlock(blocks.StructBlock):
#     heading = blocks.CharBlock(required=False)
#     paragraph = blocks.RichTextBlock(required=False)
#     background_image = ImageChooserBlock()
# 
#     class Meta:
#         app_label = 'bootstrap_business_casual'
#         template = 'bootstrap_business_casual/blocks/business_casual_signup_block.html'
# 
# 
# class BootstrapBusinessCasualContactBlock(blocks.StructBlock):
#     title = blocks.CharBlock(required=False)
#     paragraph = blocks.RichTextBlock(required=False)
#     address = blocks.TextBlock()
#     email = blocks.CharBlock()
#     phone = blocks.CharBlock()
#     SOCIAL_MEDIA = (
#         ('fab fa-facebook-f', 'Facebook'),
#         ('fa-instagram', 'Instagram'),
#         ('fab fa-linkedin', 'LinkedIn'),
#         ('fab fa-twitter', 'Twitter'),
#         ('fab fa-pinterest', 'Pinterest'),
#         ('fab fa-youtube', 'Youtube'),
#         ('fab fa-github', 'GitHub'),
#         ('fab fa-gitlab', 'GitLab'),
#     )
#     social_media = blocks.ListBlock(blocks.StructBlock([
#         ('social_media', blocks.ChoiceBlock(SOCIAL_MEDIA)),
#         ('social_link', blocks.URLBlock()),
#     ], required=False))
# 
#     def get_context(self, value, parent_context=None):
#         context = super().get_context(value, parent_context=parent_context)
#         address_query = value['address']
# 
#         # Remove all non-word characters (everything except numbers and letters)
#         import re
#         address_query = re.sub(r"[^\w\s]", '', address_query)
# 
#         # Replace all runs of whitespace with a single dash
#         address_query = re.sub(r"\s+", '+', address_query)
# 
#         context['value']['address_query'] = address_query
#         return context
# 
#     class Meta:
#         app_label = 'bootstrap_business_casual'
#         template = 'bootstrap_business_casual/blocks/business_casual_contact_block.html'


class BootstrapBusinessCasualPage(Page):
    body = StreamField([
        ('masthead', BootstrapBusinessCasualMastheadBlock()),
        ('carousel', BootstrapCommonCarouselBlock()),
        ('call', BootstrapBusinessCasualCallBlock()),
        ('about', BootstrapBusinessCasualAboutBlock()),
        ('products', BootstrapBusinessCasualProductsBlock()),
        # ('featured', BootstrapBusinessCasualFeaturedBlock()),
        ('section', BootstrapCommonTextSectionBlock()),
        # ('signup', BootstrapBusinessCasualSignupBlock()),      # Not functional on static site
        # ('contact', BootstrapBusinessCasualContactBlock()),
        ('grid', BootstrapCommonGridRowBlock()),
        ('pricing', BootstrapCommonPriceRowBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    seo_title = 'Bootstrap Business Casual Page'

