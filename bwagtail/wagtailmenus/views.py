from django import forms
from wagtail.core.models import Site


class SiteSwitchForm(forms.Form):
    site = forms.ChoiceField(choices=[])

    class Media:
        js = [
            'wagtailmenus/js/site-switcher.js',
        ]

    def __init__(self, current_site, url_helper, **kwargs):
        initial = {'site': url_helper.get_action_url('edit', current_site.pk)}
        super().__init__(initial=initial, **kwargs)
        sites = []
        for site in Site.objects.filter(current_site):
            sites.append((url_helper.get_action_url('edit', site.pk), site))
        self.fields['site'].choices = sites
