# Generated by Django 2.1.5 on 2019-01-22 12:26

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
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
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('banner_color', models.CharField(blank=True, help_text='Fill in a hex colour value', max_length=6, null=True)),
                ('include_footer', models.BooleanField(null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
                ('site_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='footer',
            name='site_settings',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer', to='settings.SiteSettings'),
        ),
    ]