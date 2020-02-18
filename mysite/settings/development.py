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





