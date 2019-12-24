from .base import *
import os
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar', 'dal', 'dal_select2',
]

 
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
    'SHOW_COLLAPSED': True,
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql', 
#         'HOST': 'localhost',      
#         'NAME': 'acc_court',
#         'USER': os.getenv('POSTGRES_USERNAME'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#     }
# }

