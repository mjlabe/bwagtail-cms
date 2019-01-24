# Generated by Django 2.1.4 on 2018-12-17 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('bootstrap_grayscale', '0049_auto_20181217_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('fas fa-phone', 'Phone'), ('fas fa-envelope', 'Email'), ('fab fa-facebook-f', 'Facebook'), ('fa-instagram', 'Instagram'), ('fab fa-linkedin', 'LinkedIn'), ('fab fa-twitter', 'Twitter'), ('fab fa-pinterest', 'Pinterest'), ('fab fa-github', 'GitHub'), ('fab fa-gitlab', 'GitLab')], max_length=50)),
                ('contact_info', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.ManyToManyField(to='bootstrap_grayscale.ContactInfo'),
        ),
        migrations.AddField(
            model_name='contact',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site'),
        ),
    ]