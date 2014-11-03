# Django settings for whiskeyengine project.
import os
import sys
import dj_database_url

DEBUG = os.environ.get('DEBUG',False)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Loren Davie','loren@axilent.com'),
)
MANAGERS = ADMINS

# ======
# = DB =
# ======
if os.environ.get('WHISKEYENGINE_RUNLOCAL'):
    db_engine = os.environ.get('DB_ENGINE','django.db.backends.postgresql_psycopg2')
    db_name = os.environ.get('DB_NAME','whiskeyengine')
    DATABASES = {
        'default': {
            'ENGINE': db_engine, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': db_name,                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    # override database name above
    DATABASES['default'] = dj_database_url.config()
    
ALLOWED_HOSTS = ['www.whiskey-engine.com','.whiskey-engine.com','localhost'] # need to add heroku app url

# ======================
# S3 via django-storages
# ======================

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', 'axilent_whiskey_engine_static')
STATIC_HOST = os.environ.get('WHISKEYENGINE_STATIC_HOST','//s3.amazonaws.com')

STATIC_URL = '/static/'
local_static = os.environ.get('WHISKEYENGINE_LOCALSTATIC',None)
if not local_static:
    STATIC_URL = '%s/%s/' % (STATIC_HOST,AWS_STORAGE_BUCKET_NAME)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_ROOT = os.environ.get('WHISKEYENGINE_WEB_STATIC_ROOT','')



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = os.environ.get('WHISKEY_URLCONF','whiskeyengine.urls')

WSGI_APPLICATION = 'whiskeyengine.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'storages',
    'south',
    'gunicorn',
    'djax',
    'whiskeyengine',
)

TEMPLATE_CONTEXT_PROCESSORS =(
        'django.core.context_processors.static',
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler'
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream':sys.stdout,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'whiskeyengine': {
            'handlers': ['console'],
            'level':'DEBUG',
            'propagate':True,
        },
        'djax': {
            'handlers': ['console'],
            'level':'DEBUG',
            'propagate': True,
        },
    }
}

# ===========
# = Axilent =
# ===========
AXILENT_API_KEY = os.environ.get('AXILENT_API_KEY')
