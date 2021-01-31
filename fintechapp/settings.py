"""
Django settings for fintechapp project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
# from companies import dashboard
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3w^xk8yf5m99l_ou7vxohqj4itt++a*v&jrkw)#_%phbp@n69p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['*']
=======
ALLOWED_HOSTS = []
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d


# Application definition

INSTALLED_APPS = [
    'csvimport',
    'jet.dashboard',
    'jet',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_gis',
    'oauth2_provider',
    'mathfilters',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'apps.endpoints',
    'apps.ml',
    'companies',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fintechapp.urls'

JET_DEFAULT_THEME = 'light-green'
JET_SIDE_MENU_COMPACT = True
# JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': { 
                'custom_tags':'companies.template_tags.custom_tags'
            }
            
        },
    },
]

WSGI_APPLICATION = 'fintechapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
<<<<<<< HEAD
        'USER' : 'postgres',
        # 'NAME': 'finapp',
        # 'PASSWORD': 'postgres', 
        # 'HOST':  'localhost',
        'NAME': 'fintech',
        'PASSWORD':  'fintech123456789',
        'HOST':  'fintech.coxeytfzdoap.eu-west-2.rds.amazonaws.com',
        'PORT': 5432,

=======
        'NAME': 'finapp',
        'USER' : 'postgres',
        'PASSWORD': 'postgres', 
        'HOST':  'localhost',
        # 'PASSWORD':  'vap123456789',
        # 'HOST':  'vap.coxeytfzdoap.eu-west-2.rds.amazonaws.com', 
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
    }
}


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
STATIC_FILES = '/static/'
STATIC_ROOT = 'static'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Gmail SMTP Server
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'mpasiinnocent@gmail.com'
EMAIL_HOST_PASSWORD = 'Greatse@1#'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER



# REST_FRAMEWORK = {
#       'DEFAULT_AUTHENTICATION_CLASSES': (
#        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#        'rest_framework.authentication.BasicAuthentication',
#        'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 20, 
    
#     'DEFAULT_PARSER_CLASSES': (
#     'rest_framework.parsers.JSONParser',
#     'rest_framework.parsers.FormParser',
#     'rest_framework.parsers.MultiPartParser',
# ),

# }

#oAuth2 expiration
OAUTH_ACCESS_TOKEN_MODEL = 'oauth2_provider.models.AccessToken'
OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS' : 86400,
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}
MAP_WIDGETS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", "gweru"),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'zw'}}),
        ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyC9ZFOeEouLH8gYosPqixfP86djN8iZCVk"
    
}