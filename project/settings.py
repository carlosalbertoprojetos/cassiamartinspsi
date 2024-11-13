from pathlib import Path
import os
import dj_database_url

# from decouple import config

# import environ

# env = environ.Env()
# environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y@m(k4()e#y1c*+=n(1f5g9qkeebvh2%y(_)8wmi-m^$q_pi0@"
# SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]  # ← Updated!

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "dados",
    # apps de terceiros
    "django_json_widget",
    "ckeditor",
    "ckeditor_uploader",
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

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "templates_tags": "project.templatetags.templates_tags",
            },
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "cassiamartinspsi",
#         "USER": "postgres",
#         "PASSWORD": "admin",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES["default"] = dj_database_url.config()

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

THOUSAND_SEPARATOR = (".",)
DECIMAL_SEPARATOR = ","
USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "staticfiles_build")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "project/static"),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": "full",
        "height": 300,
    },
}


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"  # Servidor SMTP
EMAIL_PORT = 587  # Porta do servidor SMTP
EMAIL_USE_TLS = True  # Usar TLS
EMAIL_HOST_USER = "seuemail@gmail.com"  # Seu e-mail
EMAIL_HOST_PASSWORD = "sua_senha_ou_senha_do_app"  # Sua senha ou senha do app
DEFAULT_FROM_EMAIL = "seuemail@gmail.com"
