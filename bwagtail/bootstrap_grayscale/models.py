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
from bootstrap_blog.models import *


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
        icon = 'title'


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


class BootstrapGrayscalePostPage(BootstrapPostPage):
    template = 'bootstrap_grayscale/bootstrap_grayscale_post_page.html'


class BootstrapGrayscaleBlogPage(BootstrapBlogPage):
    template = 'bootstrap_grayscale/bootstrap_grayscale_blog_page.html'
    subpage_types = ['BootstrapGrayscalePostPage']

    def get_context(self, request, *args, **kwargs):
        context = super(BootstrapGrayscaleBlogPage, self).get_context(request)

        # Get the full unpaginated listing of resource pages as a queryset -
        # replace this with your own query as appropriate
        # limit to 1000 resources
        all_resources = BootstrapGrayscalePostPage.objects.live().order_by('-first_published_at')[:1000]

        paginator = Paginator(all_resources, 10)  # Show 10 resources per page

        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resources = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resources = paginator.page(paginator.num_pages)

        # make the variable 'resources' available on the template
        context['resources'] = resources

        return context


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
        ('body', AlignedParagraphBlock()),
        # ('body', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    show_in_menus_default = True

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    seo_title = 'Bootstrap Grayscale Page'

    subpage_types = ['BootstrapGrayscalePage', 'BootstrapGrayscaleBlogPage']
