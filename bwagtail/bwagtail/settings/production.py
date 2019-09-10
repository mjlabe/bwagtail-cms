from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kr$3$hlfj=o!_==j566ev8c8ynd8*abdjfiurn4!nl#d'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

try:
    from .local import *
except ImportError:
    pass
