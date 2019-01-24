from django.db import connection
from django_currentuser.middleware import get_current_user
from wagtail.core.models import Site


def get_user_sites(current_user):
    if current_user.is_superuser:
        return Site.objects.all()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            select
              distinct s.id
            from wagtailcore_site s
            inner join wagtailcore_grouppagepermission gpp
              on gpp.page_id = s.root_page_id
            inner join auth_group ag
              on ag.id = gpp.group_id
            inner join auth_user_groups aug
              on aug.group_id = ag.id
            inner join auth_user au
              on au.id = aug.user_id
            where au.id = %s;
            """, [current_user.id]
        )
        result = cursor.fetchall()
    site_ids = [s[0] for s in result]
    return [site for site in Site.objects.filter(pk__in=site_ids)]
