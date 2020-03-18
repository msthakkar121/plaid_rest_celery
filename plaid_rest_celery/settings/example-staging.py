from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sherlocked'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

# time zone settings

TIME_ZONE = 'Asia/Calcutta'

USE_TZ = True

# celery and broker configurations
BROKER_USER = os.environ.get("BROKER_USER", "user")
BROKER_PASSWORD = os.environ.get("BROKER_PASSWORD", "password")
BROKER_HOST = os.environ.get("BROKER_HOST", "0.0.0.0")
BROKER_PORT = os.environ.get("BROKER_PORT", "5672")
BROKER_VHOST = os.environ.get("BROKER_VHOST", "/")

CELERY_BROKER_URL=f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/{BROKER_VHOST}"

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = os.environ.get("TIME_ZONE", "Asia/Calcutta")
