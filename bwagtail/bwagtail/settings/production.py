from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kr$3$hlfj=o!_==j566ev8c8ynd8*k9q=0i36gv16fb32!nl#d'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['bloodyreapercomics.com, www.bloodyreapercomics.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = '/home/brc/bwag/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/home/brc/bwag/media/'
MEDIA_URL = '/media/'

try:
    from .local import *
except ImportError:
    pass
