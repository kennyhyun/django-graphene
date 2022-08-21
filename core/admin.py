import os
from django.contrib.admin import AdminSite
from django.contrib.admin.apps import AdminConfig
from django.utils.translation import ugettext_lazy

ADMIN_SITE_TITLE = os.environ.get('ADMIN_SITE_TITLE', 'Django Administration')

class CustomAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy(ADMIN_SITE_TITLE)

    # Text to put in each page's <h1> (and above login form).
    #site_header = ugettext_lazy(ADMIN_SITE_TITLE)

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy(ADMIN_SITE_TITLE + ' Administration')

class AdminConfig(AdminConfig):
    default_site = 'core.admin.CustomAdminSite'

admin_site = CustomAdminSite()
