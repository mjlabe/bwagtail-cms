# Generated by Django 2.1.5 on 2019-03-04 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_blog', '0003_remove_bootstrappostpage_header_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootstrapblogpage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bootstrapblogpage',
            name='header_image',
        ),
    ]
