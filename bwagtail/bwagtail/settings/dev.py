from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kr$3$hlfj=o!_==j86_evacxynd@*k4q=0ie6gv56fb&2!nl#d'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# STATIC_ROOT = '/home/brc/bwag/static/'
# STATIC_URL = '/static/'
#
# MEDIA_ROOT = '/home/brc/bwag/media/'
# MEDIA_URL = '/media/'

try:
    from .local import *
except ImportError:
    pass
