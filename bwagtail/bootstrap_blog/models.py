from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.core.models import Page
# TODO: Add font awesome chooser
from wagtail.images.edit_handlers import ImageChooserPanel


class BootstrapBlogPage(Page):
    # header_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )
    # description = models.CharField(max_length=255, blank=True, )

    content_panels = Page.content_panels

    # content_panels = Page.content_panels + [
    #     ImageChooserPanel('header_image'),
    #     FieldPanel('description')
    # ]

    class Meta:
        abstract = True


class BootstrapPostPage(Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = RichTextField(blank=True)
    created_data = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        abstract = True
