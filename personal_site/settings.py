

import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# URL static files
STATIC_ROOT = "/app/static/"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

PROJECT_DIR = os.path.dirname(__file__).decode('utf-8')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1cz1-fpofmpfpmfmp'
DEBUG = False

ADMINS = (
    ('Danilo Bustos', 'dbustos10@gmail.com'),
)


TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'personal_site.urls'

WSGI_APPLICATION = 'personal_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'd3fm0u67tb6ndl',                      # Or path to database file if using sqlite3.
         'USER': 'zsnsvplamuwjsq',                      # Not used with sqlite3.
         'PASSWORD': '947wY90OmoDAoM0ltFwzsropSU',                  # Not used with sqlite3.
         'HOST': 'ec2-54-83-33-14.compute-1.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
         'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
     }
}

"""
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'personal_site',                      # Or path to database file if using sqlite3.
         'USER': 'root',                      # Not used with sqlite3.
         'PASSWORD': '123456',                  # Not used with sqlite3.
         'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
         'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
     }
}
"""

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, "static"),
    #'/Users/danilobustos/personal_site/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(os.path.dirname(__file__), 'templates')
    # SITE_PATH+'/usach/templates'
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


