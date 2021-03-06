from django import forms
from django.urls import reverse

from wagtail.core.models import Site
from bwagtail.get_user_sites import get_user_sites


class SiteSwitchForm(forms.Form):
    site = forms.ChoiceField(choices=[])

    class Media:
        js = [
            'wagtailsettings/js/site-switcher.js',
        ]

    def __init__(self, current_site, model, user, **kwargs):
        initial_data = {'site': self.get_change_url(current_site, model)}
        super().__init__(initial=initial_data, **kwargs)
        sites = [(self.get_change_url(site, model), site)
                 for site in get_user_sites(user)]
        self.fields['site'].choices = sites

    @classmethod
    def get_change_url(cls, site, model):
        return reverse('wagtailsettings:edit', args=[
            model._meta.app_label, model._meta.model_name, site.pk])
