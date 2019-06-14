from .base import *

DEBUG = False

ALLOWED_HOSTS = ['courtcasemanagement.herokuapp.com', ]

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)