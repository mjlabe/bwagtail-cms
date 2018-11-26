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


class GrayscaleMastheadBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    subheading = blocks.RichTextBlock(required=False)
    background_image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_masthead_block.html'


class GrayscaleAboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image_with_transparent_background = ImageChooserBlock(required=False)

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_about_block.html'


class GrayscaleFeaturedLargeRowBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/featured/grayscale_featured_large_row_block.html'
        label = 'Featured Large Row'


class GrayscaleFeaturedSmallRowLeftBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/featured/grayscale_featured_small_row_left_block.html'
        label = 'Features Small Row (Image Left)'


class GrayscaleSmallRowRightBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/featured/grayscale_featured_small_row_right_block.html'
        label = 'Featured Small Row (Image Right)'


class GrayscaleFeaturedBlock(blocks.StructBlock):
    featured = blocks.StreamBlock([
        ('featured_row_large', GrayscaleFeaturedLargeRowBlock()),
        ('featured_row_left', GrayscaleFeaturedSmallRowLeftBlock()),
        ('featured_row_right', GrayscaleSmallRowRightBlock()),
    ])

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/featured/grayscale_featured_block.html'
        label = 'Freatured Multi Row'


class GrayscaleSignupBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    background_image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_signup_block.html'


class GrayscaleContactBlock(blocks.StructBlock):
    address = blocks.CharBlock()
    email = blocks.CharBlock()
    phone = blocks.CharBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_contact_block.html'


class GrayscalePage(Page):
    body = StreamField([
        ('masthead', GrayscaleMastheadBlock()),
        ('about', GrayscaleAboutBlock()),
        # ('featured', GrayscaleFeaturedBlock()),
        ('featured_multi_row', GrayscaleFeaturedBlock()),
        ('signup', GrayscaleSignupBlock()),
        ('contact', GrayscaleContactBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
