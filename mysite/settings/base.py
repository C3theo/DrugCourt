"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv
import logging.config
from mysite.logs import formatter
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY',
                       'jnq#vs9tmq!3-dll70l^m^!2j*%i+#o*+8v)21d@l^c91tls=1')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS = [
    # standard django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # drug court apps
    'intake.apps.IntakeConfig',
    'core.apps.CoreConfig',
    'scribe.apps.ScribeConfig',
    # treatment
    # court
    # 'profiles.apps.ProfileConfig'

    # third-party apps
    'crispy_forms',
    'django_filters',
    'django_tables2',
    'django_fsm',
    'django_extensions',
    # 'betterforms',
    # 'guardian',
    'behave_django',
    # 'material',
    # 'material.frontend',
    # 'viewflow',
    # 'viewflow.frontend',

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'ATOMIC_REQUEST': True,
#     }
# }


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'core:home'
LOGIN_URL = 'login'

ANONYMOUS_USER_NAME = None
# GUARDIAN_MONKEY_PATCH = False

# For fields added to custom user model
# GUARDIAN_GET_INIT_ANONYMOUS_USER = 'profiles.models.get_anonymous_user_instance'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'sql': {
            '()': 'mysite.logs.formatter.SQLFormatter',
            'format': '\n%(sql)s\n',
        },
        'sourcetrace': {
            'format': '-'*80 + '\n%(sql)s\n' + '-'*80 + '\n\nStacktrace of SQL query producer:\n' + '-'*80 + '%(sourcetrace)s' + '-'*80 + '\n'+'-'*80 + '\n'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'sql': {
            'class': 'logging.StreamHandler',
            'formatter': 'sql',
            'level': 'DEBUG',
        },
        'django.db.sourcetrace': {
            'class': 'logging.StreamHandler',
            'formatter': 'sourcetrace'
        },
    },
    'root' : {
        'level' : 'DEBUG',
        'handlers' : ['console']
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['sql'], #django.db.sourcetrace
            'level': 'ERROR',
            'propagate': False,
        },

        # 'django.db.backends.schema': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    }
}



# LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()
# logging.config.dictConfig({
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'sql': {
#             '()': 'mysite.logs.SQLFormatter',
#             'format': '[%(duration).3f] %(statement)s]'
#         }},
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#         'sql': {
#             'class': 'logging.StreamHandler',
#             'foramtter': 'sql',
#             'level': 'DEBUG',
#             # 'filename': 'logconfig.log',
#             # 'formatter': 'precise',
#             # 'maxBytes': 1024,
#             # 'backupCount': 3,
#         },
#     },
#     'loggers': {
#         'djanog.db.backends': {
#             'level': 'DEBUG',
#             'handlers': ['sql'],
#             # required to avoid double logging with root logger
#             'propagate': False,
#         },
#     },
#     'django.db.backends.schema': {
#         'handlers': ['console'],
#         'level': 'DEBUG',
#         'propagate': False,
#     },
#     # 'root': {'handlers': ['console']},
# },
# )
