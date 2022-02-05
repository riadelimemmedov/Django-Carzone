"""
Django settings for carzone project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from logging import critical
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0trx3q+ol53)ue*-s0ms&_6(tuql7bkjwew97m=tt#$8n^w4b('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'pages.apps.PagesConfig',
    'cars.apps.CarsConfig',
    'accountuser.apps.AccountuserConfig',
    'contacts.apps.ContactsConfig',
    
    'ckeditor',
    'multiselectfield',
    'django.contrib.humanize',#https://simpleisbetterthancomplex.com/tips/2016/05/09/django-tip-2-humanize.html => reqemlerde cevirmeler eleyir bu paket yeni humanize paketi

    #AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    #Providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'carzone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.team_pic',
            ],
        },
    },
]

WSGI_APPLICATION = 'carzone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'carzone_db',#collectionun adi
#         'USER':'postgres',#postgres girdiyim ad defaultda yeni
#         'PASSWORD': 'riad123321',
#         'HOST':'localhost'
#     }
# }

DATABASES = {'default' : dj_database_url.config(default='postgres://postgres:riad123321@localhost/carzone_db')}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'pages')
]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#?LOGIN_REDIRECT_URL
LOGIN_REDIRECT_URL = 'accountuser:dashboardView'

CKEDITOR_CONFIGS = {#ckeditora code yazmag desteyi elave edeceyimiz ucun bunu bura yazdig yazmasag icaze vermir CKEDITOR
    "default": {
        "removePlugins": "stylesheetparser",
        'allowedContent':True,
        'width':'100%'#genislik form qeder olacag form deyisse ckeditorun olcusude deysecey
    }
}

#env/Scripts/activate

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR:'danger',
    messages.INFO:'info',
    messages.SUCCESS:'success',
}


SITE_ID = 1

#?Send Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'riadalimammedovriad@gmail.com'
EMAIL_HOST_PASSWORD = 'riad18899!'
EMAIL_USE_TLS = True

#whitenoise settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
