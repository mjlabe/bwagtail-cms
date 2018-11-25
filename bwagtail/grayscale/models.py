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
    heading = blocks.CharBlock()
    subheading = blocks.RichTextBlock()
    background_image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_masthead_block.html'


class GrayscaleAboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image_with_transparent_background = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_about_block.html'


class GrayscaleFeaturedBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        app_label = 'grayscale'
        template = 'grayscale/blocks/grayscale_featured_block.html'


# class GrayscaleFeaturedRowBlock(blocks.StructBlock):
#     heading = blocks.CharBlock()
#     paragraph = blocks.RichTextBlock()
#     image = ImageChooserBlock()
#
#     class Meta:
#         app_label = 'grayscale'
#         template = 'grayscale/blocks/grayscale_featured_row_block.html'
#
#
# class GrayscaleFeaturedMultiRowBlock(Page):
#     featured_multi_row = blocks.StructBlock([
#         ('featured_row', GrayscaleFeaturedRowBlock()),
#     ], template='grayscale/blocks/grayscale_featured_multi_row_block.html')


class GrayscalePage(Page):
    body = StreamField([
        ('masthead', GrayscaleMastheadBlock()),
        ('about', GrayscaleAboutBlock()),
        ('featured', GrayscaleFeaturedBlock()),
        # ('featured_multi_row', GrayscaleFeaturedMultiRowBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
