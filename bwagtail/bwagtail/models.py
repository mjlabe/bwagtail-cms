from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting


class ContactInfo(models.Model):
    CONTACT_CHOICES = (
        ('fas fa-phone', 'Phone'),
        ('fas fa-envelope', 'Email'),
        ('fab fa-facebook-f', 'Facebook'),
        ('fa-instagram', 'Instagram'),
        ('fab fa-linkedin', 'LinkedIn'),
        ('fab fa-twitter', 'Twitter'),
        ('fab fa-pinterest', 'Pinterest'),
        ('fab fa-github', 'GitHub'),
        ('fab fa-gitlab', 'GitLab'),
    )

    contact_type = models.CharField(choices=CONTACT_CHOICES, max_length=50)
    contact_info = models.CharField(max_length=50)

    # facebook = models.URLField(
    #     help_text='Your Facebook page URL')
    # instagram = models.CharField(
    #     max_length=255, help_text='Your Instagram username, without the @')
    # trip_advisor = models.URLField(
    #     help_text='Your Trip Advisor page URL')
    # youtube = models.URLField(
    #     help_text='Your YouTube channel or user account URL')


@register_setting
class Contact(BaseSetting):
    contact = models.ManyToManyField(ContactInfo)
