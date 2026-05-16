"""
Django settings for project project.
"""

from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-dnu8!q7n12e7bog-st+a&5@uk8gk7%0&huxfbzcqjt=!jj-e-r'

DEBUG = True

# ALLOWED HOSTS
ALLOWED_HOSTS = [
    "student-management-django-backend-1.onrender.com",
    "127.0.0.1",
    "localhost",
]

# INSTALLED APPS
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD PARTY APPS
    'rest_framework',
    'corsheaders',

    # LOCAL APPS
    'app',

]

# REST FRAMEWORK
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

}

# MIDDLEWARE
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # CORS
    'corsheaders.middleware.CorsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# ROOT URL
ROOT_URLCONF = 'project.urls'

# TEMPLATES
TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]

# WSGI
WSGI_APPLICATION = 'project.wsgi.application'

# DATABASE
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }

}

# PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },

]

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# STATIC FILES
STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'