# Generated by Django 2.1.4 on 2018-12-17 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_grayscale', '0044_auto_20181217_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='info_prefix',
        ),
    ]
