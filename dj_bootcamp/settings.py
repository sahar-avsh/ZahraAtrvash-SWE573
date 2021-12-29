"""
Django settings for dj_bootcamp project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dcl7ece)*)r^2w_cz01%*%ot_@64lsp)*&tz!))s(md!*5@i1x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'jquery',
    #'location_field.apps.DefaultConfig',
    'mapbox_location_field',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'postman',
    # 'django_messages',
    # 'pinax.notifications',
    # 'django_private_chat2.apps.DjangoPrivateChat2Config',
    'widget_tweaks',
    'django_db_constraints',
    'offers',
    'profiles',
    'categorytags'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_ip_geolocation.middleware.IpGeolocationMiddleware',
]

ROOT_URLCONF = 'dj_bootcamp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'postman.context_processors.inbox',
                # 'django-starfield'
                # 'django_messages.context_processors.inbox',
            ],
        },
    },
]

# LOCATION_FIELD = {
#     'provider.mapbox.access_token': 'pk.eyJ1Ijoic2FoYXJhdnNoIiwiYSI6ImNreHFnZnNjdDJoaGwycnFrc2t4MDk1ZHUifQ.gYnfOJY6m0NQ1hsCSQUuAQ',
#     'provider.mapbox.max_zoom': 18,
#     'provider.mapbox.id': 'mapbox.streets',
# }

MAPBOX_KEY = "pk.eyJ1Ijoic2FoYXJhdnNoIiwiYSI6ImNreHFnZnNjdDJoaGwycnFrc2t4MDk1ZHUifQ.gYnfOJY6m0NQ1hsCSQUuAQ"  

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# EMAIL_BACKEND so allauth can proceed to send confirmation emails
# ONLY for development/testing use console 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_SSL = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = ''
# EMAIL_HOST_PASSWORD = ''

# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email' 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

LOGIN_REDIRECT_URL = '/timeline/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/profiles/edit/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_FORMS = {
    'signup': 'profiles.forms.CustomSignupForm',
    'login': 'profiles.forms.CustomLoginForm'
}

WSGI_APPLICATION = 'dj_bootcamp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': '37373737scR7',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')