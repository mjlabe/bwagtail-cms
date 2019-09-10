from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import capfirst
from django.utils.translation import ugettext as _

from wagtail.admin import messages
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.core.models import Site
from wagtail.contrib.settings.views import get_model_from_url_params, get_setting_edit_handler, user_can_edit_setting_type
from .forms import SiteSwitchForm
from bwagtail.get_user_sites import get_user_sites


def edit_current_site(request):
    # Redirect the user to the edit page for the current site
    # (or the current request does not correspond to a site, the first site in the list)
    user_sites = get_user_sites(request.user)
    default_site = request.site if request.site in user_sites else None
    try:
        site = default_site or user_sites[0]
    except IndexError:
        site = None

    if not site:
        messages.error(request, _("This setting could not be opened because there is no site defined."))
        return redirect('wagtailadmin_home')
    # TODO: this redirect doesn't seem to work
    return edit(request, site.pk)


def edit(request, site_pk):
    # get user
    user = request.user
    app_name = 'settings'
    model_name = 'sitesettings'
    # site = request.site or Site.objects.first()
    # if not site:
    #     messages.error(request, _("This setting could not be opened because there is no site defined."))
    #     return redirect('wagtailadmin_home')

    model = get_model_from_url_params(app_name, model_name)
    if not user_can_edit_setting_type(request.user, model):
        raise PermissionDenied
    site = get_object_or_404(Site, pk=site_pk)

    setting_type_name = model._meta.verbose_name

    instance = model.for_site(site)
    edit_handler = get_setting_edit_handler(model)
    form_class = edit_handler.get_form_class()

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                _("{setting_type} updated.").format(
                    setting_type=capfirst(setting_type_name),
                    instance=instance
                )
            )
            return redirect('wagtailsettings:edit', app_name, model_name, site.pk)
        else:
            messages.validation_error(
                request, _("The setting could not be saved due to errors."), form
            )
            edit_handler = edit_handler.bind_to_instance(
                instance=instance, form=form, request=request)
    else:
        form = form_class(instance=instance)
        edit_handler = edit_handler.bind_to_instance(
            instance=instance, form=form, request=request)

    # Show a site switcher form if there are multiple sites
    site_switcher = None
    if Site.objects.count() > 1:
        site_switcher = SiteSwitchForm(site, model, user)

    return render(request, 'wagtailsettings/edit.html', {
        'opts': model._meta,
        'setting_type_name': setting_type_name,
        'instance': instance,
        'edit_handler': edit_handler,
        'form': form,
        'site': site,
        'site_switcher': site_switcher,
        'tabbed': isinstance(edit_handler, TabbedInterface),
    })
