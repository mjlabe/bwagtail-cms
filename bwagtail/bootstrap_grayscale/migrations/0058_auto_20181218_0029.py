# Generated by Django 2.1.4 on 2018-12-18 00:29

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
        ('bootstrap_grayscale', '0057_contactinfo_info_prefix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('include_footer', models.BooleanField()),
                ('contact_type', models.CharField(choices=[('fas fa-phone', 'Phone'), ('fas fa-envelope', 'Email'), ('fab fa-facebook-f', 'Facebook'), ('fa-instagram', 'Instagram'), ('fab fa-linkedin', 'LinkedIn'), ('fab fa-twitter', 'Twitter'), ('fab fa-pinterest', 'Pinterest'), ('fab fa-youtube', 'Youtube'), ('fab fa-github', 'GitHub'), ('fab fa-gitlab', 'GitLab')], max_length=50)),
                ('contact_info', models.CharField(max_length=50)),
                ('info_prefix', models.CharField(editable=False, max_length=10)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('site_name', models.CharField(max_length=50)),
                ('banner_colour', models.CharField(blank=True, help_text='Fill in a hex colour value', max_length=6, null=True)),
                ('site_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='contact',
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='SiteSettings',
        ),
        migrations.DeleteModel(
            name='ContactInfo',
        ),
        migrations.AddField(
            model_name='header',
            name='site_settings',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='header', to='bootstrap_grayscale.SiteSettings'),
        ),
        migrations.AddField(
            model_name='footer',
            name='site_settings',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer', to='bootstrap_grayscale.SiteSettings'),
        ),
    ]