# Generated by Django 2.1.5 on 2019-03-03 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wag_custom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='site_logo',
        ),
    ]
