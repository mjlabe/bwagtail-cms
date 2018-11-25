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
        template = 'grayscale/blocks/grayscale_masthead_block.html'


class GrayscalePage(Page):
    body = StreamField([
        ('masthead', GrayscaleMastheadBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
