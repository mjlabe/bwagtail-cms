from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.blocks import ImageChooserBlock


# TODO: Add font awesome chooser
from wagtail.images.edit_handlers import ImageChooserPanel


class BootstrapCommon2ColumnBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading1', blocks.CharBlock(required=False)),
        ('paragraph1', blocks.RichTextBlock(required=False)),
        ('image1', ImageChooserBlock(required=False)),
        ('link1', blocks.PageChooserBlock(required=False)),

        ('heading2', blocks.CharBlock(required=False)),
        ('paragraph2', blocks.RichTextBlock(required=False)),
        ('image2', ImageChooserBlock(required=False)),
        ('link2', blocks.PageChooserBlock(required=False))
        ]))

    class Meta:
        template = 'bootstrap_common/blocks/grid/bootstrap_common_2_column_block.html'
        label = '2 Column'
        icon = 'grip'


class BootstrapCommon3ColumnBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading1', blocks.CharBlock(required=False)),
        ('paragraph1', blocks.RichTextBlock(required=False)),
        ('image1', ImageChooserBlock(required=False)),
        ('link1', blocks.PageChooserBlock(required=False)),

        ('heading2', blocks.CharBlock(required=False)),
        ('paragraph2', blocks.RichTextBlock(required=False)),
        ('image2', ImageChooserBlock(required=False)),
        ('link2', blocks.PageChooserBlock(required=False)),

        ('heading3', blocks.CharBlock(required=False)),
        ('paragraph3', blocks.RichTextBlock(required=False)),
        ('image3', ImageChooserBlock(required=False)),
        ('link3', blocks.PageChooserBlock(required=False))
        ]))

    class Meta:
        template = 'bootstrap_common/blocks/grid/bootstrap_common_3_column_block.html'
        label = '3 Column'
        icon = 'grip'


class BootstrapCommon4ColumnBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading1', blocks.CharBlock(required=False)),
        ('paragraph1', blocks.RichTextBlock(required=False)),
        ('image1', ImageChooserBlock(required=False)),
        ('link1', blocks.PageChooserBlock(required=False)),

        ('heading2', blocks.CharBlock(required=False)),
        ('paragraph2', blocks.RichTextBlock(required=False)),
        ('image2', ImageChooserBlock(required=False)),
        ('link2', blocks.PageChooserBlock(required=False)),

        ('heading3', blocks.CharBlock(required=False)),
        ('paragraph3', blocks.RichTextBlock(required=False)),
        ('image3', ImageChooserBlock(required=False)),
        ('link3', blocks.PageChooserBlock(required=False)),

        ('heading4', blocks.CharBlock(required=False)),
        ('paragraph4', blocks.RichTextBlock(required=False)),
        ('image4', ImageChooserBlock(required=False)),
        ('link4', blocks.PageChooserBlock(required=False))
        ]))

    class Meta:
        template = 'bootstrap_common/blocks/grid/bootstrap_common_4_column_block.html'
        label = '4 Column'
        icon = 'grip'


class BootstrapCommon8ColumnBlock(blocks.StructBlock):
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading1', blocks.CharBlock(required=False)),
        ('paragraph1', blocks.RichTextBlock(required=False)),
        ('image1', ImageChooserBlock(required=False)),
        ('link1', blocks.PageChooserBlock(required=False)),

        ('heading2', blocks.CharBlock(required=False)),
        ('paragraph2', blocks.RichTextBlock(required=False)),
        ('image2', ImageChooserBlock(required=False)),
        ('link2', blocks.PageChooserBlock(required=False)),

        ('heading3', blocks.CharBlock(required=False)),
        ('paragraph3', blocks.RichTextBlock(required=False)),
        ('image3', ImageChooserBlock(required=False)),
        ('link3', blocks.PageChooserBlock(required=False)),

        ('heading4', blocks.CharBlock(required=False)),
        ('paragraph4', blocks.RichTextBlock(required=False)),
        ('image4', ImageChooserBlock(required=False)),
        ('link4', blocks.PageChooserBlock(required=False)),

        ('heading5', blocks.CharBlock(required=False)),
        ('paragraph5', blocks.RichTextBlock(required=False)),
        ('image5', ImageChooserBlock(required=False)),
        ('link5', blocks.PageChooserBlock(required=False)),

        ('heading6', blocks.CharBlock(required=False)),
        ('paragraph7', blocks.RichTextBlock(required=False)),
        ('image6', ImageChooserBlock(required=False)),
        ('link6', blocks.PageChooserBlock(required=False)),

        ('heading7', blocks.CharBlock(required=False)),
        ('paragraph7', blocks.RichTextBlock(required=False)),
        ('image7', ImageChooserBlock(required=False)),
        ('link7', blocks.PageChooserBlock(required=False)),

        ('heading8', blocks.CharBlock(required=False)),
        ('paragraph8', blocks.RichTextBlock(required=False)),
        ('image8', ImageChooserBlock(required=False)),
        ('link8', blocks.PageChooserBlock(required=False))
        ]))

    class Meta:
        template = 'bootstrap_common/blocks/grid/bootstrap_common_8_column_block.html'
        label = '8 Column'
        icon = 'grip'


class BootstrapCommonGridRowBlock(blocks.StructBlock):
    row = blocks.StreamBlock([
        ('bootstrap_common_2_column', BootstrapCommon2ColumnBlock()),
        ('bootstrap_common_3_column', BootstrapCommon3ColumnBlock()),
        ('bootstrap_common_4_column', BootstrapCommon4ColumnBlock()),
        # ('bootstrap_common_6_column', BootstrapCommon6ColumnBlock()),
        ('bootstrap_common_8_column', BootstrapCommon8ColumnBlock()),
    ])

    class Meta:
        template = 'bootstrap_common/blocks/grid/bootstrap_common_grid_row_block.html'
        label = 'Grid Row'
        icon = 'grip'


class BootstrapCommonPriceCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock()
    price = blocks.DecimalBlock()
    rate = blocks.CharBlock()
    button_text = blocks.CharBlock()

    class Meta:
        template = 'bootstrap_common/blocks/pricing/bootstrap_common_price_card_block.html'
        label = 'Price Card'


# TODO: make this a listblock
class BootstrapCommonPriceRowBlock(blocks.StructBlock):
    heading = blocks.CharBlock()
    paragraph = blocks.RichTextBlock(required=False)
    row = blocks.StreamBlock([
        ('bootstrap_common_price_block', BootstrapCommonPriceCardBlock()),
    ])

    class Meta:
        template = 'bootstrap_common/blocks/pricing/bootstrap_common_price_row_block.html'
        label = 'Pricing Row'


class BootstrapCommonTextSectionBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    button_text = blocks.CharBlock(required=False)
    button_link = blocks.PageChooserBlock(required=False)
    background_image = ImageChooserBlock(required=False)
    COLOR_CHOICES = (
        ('', 'Light'),
        ('bg-dark text-light', 'Dark'),
        ('bg-primary text-light', 'Theme')
    )
    background_color = blocks.ChoiceBlock(choices=COLOR_CHOICES, required=False)
    iframe = blocks.RawHTMLBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if value['background_color'] == 'bg-dark text-light':
            context['value']['btn_color'] = 'btn-secondary'
        elif value['background_color'] == 'bg-primary text-light':
            context['value']['btn_color'] = 'btn-light'
        else:
            context['value']['btn_color'] = 'btn-primary'
        return context

    class Meta:
        template = 'bootstrap_common/blocks/bootstrap_common_text_section_block.html'
        label = 'Section'


class BootstrapCommonCarouselBlock(blocks.StructBlock):
    masthead = blocks.BooleanBlock(required=False)
    COLOR_CHOICES = (
        ('light', 'Light'),
        ('dark', 'Dark'),
        ('theme', 'Theme')
    )
    item = blocks.ListBlock(blocks.StructBlock([
        ('heading', blocks.CharBlock(required=False)),
        ('paragraph', blocks.CharBlock(required=False)),
        ('image', ImageChooserBlock()),
        ('button_text', blocks.CharBlock(required=False)),
        ('button_link', blocks.PageChooserBlock(required=False)),
    ]))

    class Meta:
        template = 'bootstrap_common/blocks/bootstrap_common_carousel_block.html'
        label = 'Carousel'
        icon = 'image'


class AlignedParagraphBlock(blocks.StructBlock):
    alignment = blocks.ChoiceBlock([('text-center', 'Center'), ('text-justify', 'Justify'), ('text-left', 'Left'),
                                    ('text-right', 'Right')], default='text-center')
    paragraph = blocks.RichTextBlock()

    class Meta:
        template = 'bootstrap_common/blocks/bootstrap_common_paragraph.html'
        icon = 'doc-full'
