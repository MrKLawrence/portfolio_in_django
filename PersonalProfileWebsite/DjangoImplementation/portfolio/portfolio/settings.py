
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '<paste your production secret here!>'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [

]

ROOT_URLCONF = 'porfolio_project.urls'

TEMPLATES = [

]

WSGI_APPLICATION = ''

DATABASES = {

}

AUTH_PASSWORD_VALIDATORS = [

]

LANGUAGE_CODE = 'en_us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'