# Generated by Django 2.1.5 on 2019-03-08 01:12

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_grayscale', '0072_auto_20190308_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrapgrayscalepage',
            name='body',
            field=wagtail.core.fields.StreamField([('masthead', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('heading_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('subheading', wagtail.core.blocks.RichTextBlock(required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock()), ('button_text', wagtail.core.blocks.CharBlock(required=False)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_theme', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Light'), ('dark', 'Dark'), ('theme', 'Theme')], required=False))])), ('carousel', wagtail.core.blocks.StructBlock([('masthead', wagtail.core.blocks.BooleanBlock(required=False)), ('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('button_text', wagtail.core.blocks.CharBlock(required=False)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('about', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image_with_transparent_background', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('featured', wagtail.core.blocks.StructBlock([('featured', wagtail.core.blocks.StreamBlock([('featured_row_large', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')]))])))])), ('featured_row', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('image_position', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')]))])))]))]))])), ('section', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(required=False)), ('button_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Light'), ('bg-dark text-light', 'Dark'), ('bg-primary text-light', 'Theme')], required=False)), ('iframe', wagtail.core.blocks.RawHTMLBlock(required=False))])), ('contact', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('address', wagtail.core.blocks.TextBlock(required=False)), ('email', wagtail.core.blocks.CharBlock()), ('phone', wagtail.core.blocks.CharBlock()), ('social_media', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('social_media', wagtail.core.blocks.ChoiceBlock(choices=[('fab fa-facebook-f', 'Facebook'), ('fab fa-instagram', 'Instagram'), ('fab fa-linkedin', 'LinkedIn'), ('fab fa-twitter', 'Twitter'), ('fab fa-pinterest', 'Pinterest'), ('fab fa-youtube', 'Youtube'), ('fab fa-github', 'GitHub'), ('fab fa-gitlab', 'GitLab')])), ('social_link', wagtail.core.blocks.URLBlock())], required=False)))])), ('grid', wagtail.core.blocks.StructBlock([('row', wagtail.core.blocks.StreamBlock([('bootstrap_common_2_column', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.RichTextBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link1', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.RichTextBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link2', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('bootstrap_common_3_column', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.RichTextBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link1', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.RichTextBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link2', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph3', wagtail.core.blocks.RichTextBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link3', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('bootstrap_common_4_column', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.RichTextBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link1', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.RichTextBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link2', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph3', wagtail.core.blocks.RichTextBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link3', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading4', wagtail.core.blocks.CharBlock(required=False)), ('paragraph4', wagtail.core.blocks.RichTextBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link4', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('bootstrap_common_8_column', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.RichTextBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link1', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.RichTextBlock(required=False)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link2', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph3', wagtail.core.blocks.RichTextBlock(required=False)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link3', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading4', wagtail.core.blocks.CharBlock(required=False)), ('paragraph4', wagtail.core.blocks.RichTextBlock(required=False)), ('image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link4', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading5', wagtail.core.blocks.CharBlock(required=False)), ('paragraph5', wagtail.core.blocks.RichTextBlock(required=False)), ('image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link5', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading6', wagtail.core.blocks.CharBlock(required=False)), ('paragraph7', wagtail.core.blocks.RichTextBlock(required=False)), ('image6', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link6', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading7', wagtail.core.blocks.CharBlock(required=False)), ('image7', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link7', wagtail.core.blocks.PageChooserBlock(required=False)), ('heading8', wagtail.core.blocks.CharBlock(required=False)), ('paragraph8', wagtail.core.blocks.RichTextBlock(required=False)), ('image8', wagtail.images.blocks.ImageChooserBlock(required=False)), ('link8', wagtail.core.blocks.PageChooserBlock(required=False))])))]))]))])), ('pricing', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('row', wagtail.core.blocks.StreamBlock([('bootstrap_common_price_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('price', wagtail.core.blocks.DecimalBlock()), ('rate', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock())]))]))])), ('body', wagtail.core.blocks.StructBlock([('alignment', wagtail.core.blocks.ChoiceBlock(choices=[('text-left', 'Left'), ('text-left', 'Left'), ('text-center', 'Center'), ('text-justify', 'Justify')])), ('paragraph', wagtail.core.blocks.RichTextBlock())])), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]
