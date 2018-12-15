from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from bootstrap_common.models import *


class BootstrapGrayscaleMastheadBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
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


class BootstrapGrayscaleContactSocialBlock(blocks.StructBlock):
    SOCIAL_MEDIA = (
        ('fab fa-facebook-f', 'Facebook'),
        ('fab fa-github', 'GitHub'),
        ('fab fa-gitlab', 'GitLab'),
        ('fa-instagram', 'Instagram'),
        ('fab fa-linkedin', 'LinkedIn'),
        ('fab fa-twitter', 'Twitter'),
    )

    social_media = blocks.ChoiceBlock(SOCIAL_MEDIA)
    link = blocks.CharBlock()

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/grayscale_contact_social_block.html'
        label = 'Social Media Links'


class BootstrapGrayscaleContactBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    address = blocks.CharBlock()
    email = blocks.CharBlock()
    phone = blocks.CharBlock()
    SOCIAL_MEDIA = (
        ('fab fa-facebook-f', 'Facebook'),
        ('fab fa-github', 'GitHub'),
        ('fab fa-gitlab', 'GitLab'),
        ('fa-instagram', 'Instagram'),
        ('fab fa-linkedin', 'LinkedIn'),
        ('fab fa-twitter', 'Twitter'),
    )
    social_media = blocks.ListBlock(blocks.StructBlock([
        ('social_media', blocks.ChoiceBlock(SOCIAL_MEDIA)),
        ('social_link', blocks.URLBlock()),
    ], required=False))

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
