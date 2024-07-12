"""
Django settings for ARPortfolio project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path
from dotenv import dotenv_values
#from decouple import config

env_vars = dotenv_values()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cloudinary imports
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config("SECRET_KEY")
SECRET_KEY = 'o0%(pn0)@s68h!w34!k%aoop78xi!@g!48!nll%f7!wr1u!mkn'
#SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['.vercel.app']
#ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")

# Application definition
INSTALLED_APPS = [
    'cloudinary_storage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.portfolio',
    'ckeditor',
    'cloudinary',
    'django_recaptcha',
    'whitenoise',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CKEDITOR_CONFIGS = {
    'default': {
        'allowedContent': True,
        'extraAllowedContent': 'span[*]',
    }
}

EXCLUDE_FROM_MINIFYING = ('^admin/')

GZIP_CONTENT_TYPES = [
  'text/html',
  'text/css',
  'application/json',
]

ROOT_URLCONF = 'config.urls'

TEMPLATE_DIR = os.path.join(CORE_DIR, "templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'config.wsgi.application'

# For Dev
EMAILHOST_USER = env_vars.get("EMAIL_HOST_USER")
EMAILHOST_PASSWD = env_vars.get("EMAIL_HOST_PASSWORD")

# For Prod
#EMAILHOST_USER = os.environ.get("EMAIL_HOST_USER")
#EMAILHOST_PASSWD = os.environ.get("EMAIL_HOST_PASSWORD")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = EMAILHOST_USER
EMAIL_HOST_PASSWORD = EMAILHOST_PASSWD

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default" : {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME" : BASE_DIR / "db.sqlite3",
    }
}

#database_url = os.environ.get("DATABASE_URL")
#DATABASES["default"] = dj_database_url.parse(database_url, conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'

if DEBUG is False:
    STATICFILES_DIRS = [ BASE_DIR / 'static' ]
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# For Dev
RECAPTCHA_PUBLIC_KEY = env_vars.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env_vars.get("RECAPTCHA_PRIVATE_KEY")

# For Prod
# RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
# RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")

# For Dev
CLOUDINARY_CLOUDNAME = env_vars.get("CLOUD_NAME")
CLOUDINARY_APIKEY = env_vars.get("CLOUD_API_KEY")
CLOUDINARY_SECRET = env_vars.get("CLOUD_API_SECRET")

# For PROD
# CLOUDINARY_CLOUDNAME = os.environ.get("CLOUD_NAME")
# CLOUDINARY_APIKEY = os.environ.get("CLOUD_API_KEY")
# CLOUDINARY_SECRET = os.environ.get("CLOUD_API_SECRET")

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': CLOUDINARY_CLOUDNAME,
    'API_KEY': CLOUDINARY_APIKEY,
    'API_SECRET': CLOUDINARY_SECRET,
}

cloudinary.config(
    cloud_name = CLOUDINARY_CLOUDNAME,
    api_key = CLOUDINARY_APIKEY,
    api_secret = CLOUDINARY_SECRET,
)