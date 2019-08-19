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

# SQL Server
# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'CaseMgmt',
#         'HOST': 'DESKTOP-9AN0D63',
#         'INTEGRATED SECURITY': 'SSPI',
#         'OPTIONS': {
#             'driver': 'ODBC Driver 13 for SQL Server',
#         },

#     }

# }

# DATABASE_URL="Server=localhost;Database=master;Trusted_Connection=True"