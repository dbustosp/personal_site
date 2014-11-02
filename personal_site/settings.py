# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_DIR = os.path.dirname(__file__).decode('utf-8')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1cz1-1g-dw)t-9^uua@yanq4g#skz56m9a8jw+0g=1p-h#1wp='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (
    ('Danilo Bustos', 'dbustos10@gmail.com'),
)


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
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
         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'personal_site',                      # Or path to database file if using sqlite3.
         'USER': 'root',                      # Not used with sqlite3.
         'PASSWORD': '123456',                  # Not used with sqlite3.
         'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
         'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
     }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
