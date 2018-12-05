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
from bwagtail.bootstrap_common.models import *


class BootstrapGrayscaleMastheadBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    subheading = blocks.RichTextBlock(required=False)
    background_image = ImageChooserBlock()

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
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/featured/grayscale_featured_large_row_block.html'
        label = 'Featured Large Row'


class BootstrapGrayscaleFeaturedSmallRowLeftBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/featured/grayscale_featured_small_row_left_block.html'
        label = 'Features Small Row (Image Left)'


class BootstrapGrayscaleSmallRowRightBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/featured/grayscale_featured_small_row_right_block.html'
        label = 'Featured Small Row (Image Right)'


class BootstrapGrayscaleFeaturedBlock(blocks.StructBlock):
    featured = blocks.StreamBlock([
        ('featured_row_large', BootstrapGrayscaleFeaturedLargeRowBlock()),
        ('featured_row_left', BootstrapGrayscaleFeaturedSmallRowLeftBlock()),
        ('featured_row_right', BootstrapGrayscaleSmallRowRightBlock()),
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
    address = blocks.CharBlock()
    email = blocks.CharBlock()
    phone = blocks.CharBlock()
    social_media = blocks.StreamBlock([
        ('social_link', BootstrapGrayscaleContactSocialBlock(required=False)),
    ], required=False)

    class Meta:
        app_label = 'bootstrap_grayscale'
        template = 'bootstrap_grayscale/blocks/grayscale_contact_block.html'


class BootstrapGrayscalePage(Page):
    body = StreamField([
        ('masthead', BootstrapGrayscaleMastheadBlock()),
        ('about', BootstrapGrayscaleAboutBlock()),
        ('featured', BootstrapGrayscaleFeaturedBlock()),
        # ('featured_multi_row', BootstrapGrayscaleFeaturedBlock()),
        ('signup', BootstrapGrayscaleSignupBlock()),
        ('contact', BootstrapGrayscaleContactBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    seo_title = 'Bootstrap Grayscale Page'
