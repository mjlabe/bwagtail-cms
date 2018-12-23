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
    heading = blocks.CharBlock()
    subheading = blocks.RichTextBlock()
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
        ('heading_upper', blocks.CharBlock()),
        ('heading_lower', blocks.CharBlock()),
        ('paragraph', blocks.TextBlock(help_text='Make sure you have over 80 characters to render properly.')),
        ('image', ImageChooserBlock()),
        ]))

    class Meta:
        app_label = 'bootstrap_business_casual'
        template = 'bootstrap_business_casual/blocks/bootstrap_business_casual_products_block.html'
        label = 'Products'


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

