from __future__ import absolute_import, unicode_literals
import os
from django.core.wsgi import get_wsgi_application
from decouple import config
from whitenoise import WhiteNoise
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('SETTINGS_MODULE_PATH'))
application = get_wsgi_application()
application = WhiteNoise(application, os.path.join(settings.BASE_DIR, 'mypage/static'))