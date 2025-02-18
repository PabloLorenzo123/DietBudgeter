"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import dj_database_url # Needed to connect to postgresql.
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$%66)d0i0n1zcb^=ai^6k%2@gv8&u+zba10nu#0z$zp)hjecw!'
USDA_API_KEY = os.environ.get('USDA_API_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
IN_PROD = os.environ.get('IN_PROD') == 'True'

DEBUG = True if IN_PROD else False

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        # This setting defines the authentication mechanisms that the Django REST framework will use for securing the API
        # This means the API expects clients to authenticate by sending a JWT token with their requests.
    ),
    "DEFAULT_PERMISSION_CLASSES": {
        "rest_framework.permissions.isAuthenticated",
        # This setting defines the default permission policies for accessing API endpoints.
        # Ensures that only authenticated users (those who provide valid credentials, like a JWT token) can access the API.
    }
}

SIMPLE_JWT =  {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60 * 6),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Application definition

INSTALLED_APPS = [
    # Local apps.
    'accounts',
    'diet',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if IN_PROD:
    print("Using production database.")
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DB_URL'))
    }
else:
    print("Using development database.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Custom user model.
AUTH_USER_MODEL = 'accounts.User'

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Here will be saved the static files needed to be provided in production.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Cache and compresses staticfiles.

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
# This configuration opens your API to cross-site request forgery (CSRF) attacks because any domain can access your API with user credentials. 

# APP settings.
DEFAULT_SERVING_MEASURE = 'serving'

DIARY_SETTINGS_MAX_N_MEALS = 8

RDI = {
    "energy": 2000.0,             # Calories (kcal)
    "protein": 50.0,              # grams
    "fiber": 25.0,                # grams
    "starch": 130.0,              # grams
    "sugars": 36.0,               # grams
    "added_sugars": 24.0,          # grams
    "net_carbs": 225.0,            # grams
    "monounsaturated_fat": 25.0,   # grams
    "polyunsaturated_fat": 11.0,   # grams
    "saturated_fat": 20.0,         # grams
    "trans_fat": 0.0,              # grams (should be minimized)
    "cholesterol": 300.0,        # milligrams
    "total_fat": 70.0,             # grams
    "b1": 1.2,                    # mg (Thiamine)
    "b2": 1.3,                    # mg (Riboflavin)
    "b3": 16.0,                   # mg (Niacin)
    "b5": 5.0,                    # mg (Pantothenic Acid)
    "b6": 1.7,                    # mg
    "b12": 2.4,                   # mcg
    "choline": 425.0,             # mg
    "folate": 400.0,              # mcg
    "a": 900.0,                   # mcg (RAE - Retinol Activity Equivalents)
    "c": 90.0,                    # mg
    "d": 20.0,                    # mcg
    "e": 15.0,                    # mg
    "k": 120.0,                   # mcg
    "calcium": 1300.0,            # mg
    "chromium": 35.0,             # mcg
    "copper": 0.9,                # mg
    "iron": 18.0,                 # mg
    "magnesium": 400.0,           # mg
    "manganese": 2.3,             # mg
    "molybdenum": 45.0,           # mcg
    "phosphorus": 700.0,          # mg
    "potassium": 4700.0,          # mg
    "selenium": 55.0,             # mcg
    "sodium": 2300.0,             # mg
    "zinc": 11.0                  # mg
}