# Generated by Django 2.1.4 on 2018-12-17 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('bootstrap_grayscale', '0047_auto_20181217_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(help_text='Your Facebook page URL')),
                ('instagram', models.CharField(help_text='Your Instagram username, without the @', max_length=255)),
                ('trip_advisor', models.URLField(help_text='Your Trip Advisor page URL')),
                ('youtube', models.URLField(help_text='Your YouTube channel or user account URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Footer',
        ),
        migrations.DeleteModel(
            name='Navbar',
        ),
    ]