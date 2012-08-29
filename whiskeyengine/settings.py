# Django settings for whiskeyengine project.
import os

# =========================
# = Environment Variables =
# =========================
ENV_DEBUG = os.environ.get('DEBUG',False)
ENV_ADMIN = os.environ.get('ADMIN','ops@axilent.com')
ENV_DJANGO_KEY = os.environ.get('DJANGO_KEY','')
ENV_AXILENT_LIBRARY_KEY = os.environ.get('AXILENT_LIBRARY_KEY','')
ENV_AXILENT_PRODUCTION_KEY = os.environ.get('AXILENT_PRODUCTION_KEY','')
ENV_AXILENT_ENDPOINT = os.environ.get('AXILENT_ENDPOINT','https://www.axilent.net')

if ENV_DEBUG == 'False' or not ENV_DEBUG:
    DEBUG = False
else:
    DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# ======
# = DB =
# ======
db_engine = os.environ.get('DB_ENGINE','django.db.backends.sqlite3')
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

# ===============
# For Heroku DB =
# ===============
import dj_database_url
# override database name above
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

if 'PYTHONHOME' in os.environ:
    #default_pwd = os.environ['PYTHONHOME']
    default_pwd = '/app/'
elif 'PWD' in os.environ:
    default_pwd = os.environ['PWD']
else:
    default_pwd = ''


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
SECRET_KEY = ENV_DJANGO_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = os.environ.get('WHISKEY_URLCONF','whiskeyengine.urls')

WHISKEY_APP = os.environ.get('WHISKEY_APP','whiskeyengine')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'south',
    'gunicorn',
    WHISKEY_APP,
)

TEMPLATE_CONTEXT_PROCESSORS =(
        'django.core.context_processors.static',
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",
        )

# ===========
# = Axilent =
# ===========
AXILENT_API_KEY = ENV_AXILENT_PRODUCTION_KEY
AXILENT_ENDPOINT = ENV_AXILENT_ENDPOINT
