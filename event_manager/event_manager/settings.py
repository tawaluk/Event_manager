import os

from pathlib import Path

from celery import Celery

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%k^@-4e)*7vv*u6&q02n0_d8dg2l=(!^q_g7an&o461=qf@d3o'

DEBUG = True

ALLOWED_HOSTS = ['*', 'localhost',]

INSTALLED_APPS = [
    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'backend',
    'users',
    # additional functionality
    'rest_framework',
    'rest_framework.authtoken',
    'phonenumber_field',
    'django_filters',
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

ROOT_URLCONF = 'event_manager.urls'

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

WSGI_APPLICATION = 'event_manager.wsgi.application'

AUTH_USER_MODEL = 'users.CustomUser'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'POSTGRES',
        'USER': 'POSTGRES',
        'PASSWORD': 'POSTGRES',
        'HOST': 'db',
        'PORT': 5432,
    }
}

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'backend.permissions.CustomPermission',
    ],
}

AUTHENTICATION_BACKENDS = ['users.backend.EmailBackend']

app = Celery('event_manager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

CELERY_BROKER_URL = "redis://0.0.0.0:6379"
CELERY_RESULT_BACKEND = "redis://0.0.0.0:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
