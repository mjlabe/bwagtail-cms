from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.core.models import Page
# TODO: Add font awesome chooser
from wagtail.images.edit_handlers import ImageChooserPanel


class BootstrapPostPage(Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary = models.CharField(max_length=100, help_text='Shown on Blog/News index page.')
    body = RichTextField(blank=True)
    featured = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image', classname="full"),
        FieldPanel('featured'),
        FieldPanel('summary', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        abstract = True


class BootstrapBlogPage(Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    subtitle = models.CharField(max_length=255, blank=True, )

    show_in_menus_default = True

    # content_panels = Page.content_panels

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('subtitle')
    ]

    class Meta:
        abstract = True
