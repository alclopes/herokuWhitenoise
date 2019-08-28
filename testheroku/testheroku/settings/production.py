import os
from .common import *
import dj_database_url
from decouple import config
# import django_heroku #VER2019081308-Precisa comentar para fazer as migrações no desenv, utilizar no mamage.py o ambiente de develop

# https://devcenter.heroku.com/articles/deploying-python
# https://devcenter.heroku.com/categories/working-with-django

# ############## DEBUG
DEBUG = config('DEBUG', default=False, cast=bool)

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# ############## DataBase - Heroku
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
# DATABASE_URL = os.environ['DATABASE_URL']   #VER2019081308

#Apps Instalados
INSTALLED_APPS += [
    'whitenoise.runserver_nostatic',
]

# ############## MIDDLEWARE - whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ############## whitenoise
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ############### Activate Django-Heroku.
# django_heroku.settings(locals())

