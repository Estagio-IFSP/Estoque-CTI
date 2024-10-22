import os
import logging

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APPEND_SLASH = True

SECRET_KEY = os.environ["DJANGO_SECRET"]

DEBUG = os.environ.get("DJANGO_DEBUG", "FALSE") == "TRUE"

ALLOWED_HOSTS = [os.environ["DJANGO_HOST"]]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "huey.contrib.djhuey",
    "stockControl",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "stockControl.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "stockControl.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DJANGO_DB_NAME"],
        "USER": os.environ["DJANGO_DB_USER"],
        "PASSWORD": os.environ["DJANGO_DB_PASSWORD"],
        "HOST": os.environ.get('DJANGO_DB_HOST', ""),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_URL='login'
LOGIN_REDIRECT_URL='dashboard'
LOGOUT_REDIRECT_URL='login'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.environ.get("DJANGO_STATIC_ROOT", "/var/www/static")
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email sending configuration

# SMTP server
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_SUBJECT_PREFIX='[Estoque-CTI] '
EMAIL_HOST=os.environ["DJANGO_EMAIL_HOST"]
EMAIL_PORT=int(os.environ["DJANGO_EMAIL_PORT"])
EMAIL_HOST_USER=os.environ["DJANGO_EMAIL_HOST_USER"]
DEFAULT_FROM_EMAIL=os.environ.get("DJANGO_EMAIL_FROM", EMAIL_HOST_USER)
SERVER_EMAIL=os.environ.get("DJANGO_SERVER_EMAIL_FROM", EMAIL_HOST_USER)
EMAIL_HOST_PASSWORD=os.environ["DJANGO_EMAIL_HOST_PASSWORD"]
EMAIL_USE_TLS=os.environ.get("DJANGO_EMAIL_USE_TLS", "FALSE") == "TRUE"
EMAIL_USE_SSL=os.environ.get("DJANGO_EMAIL_USE_SSL", "FALSE") == "TRUE"
EMAIL_TIMEOUT=int(os.environ.get("DJANGO_EMAIL_TIMEOUT", "20"))

# Scheduler for periodical emails and checks
HUEY = {
    'huey_class': 'huey.SqliteHuey',
    'filename': '/tmp/huey.db',
    'immediate': False,
    'consumer': {
        'loglevel': logging.DEBUG,
    },
}
