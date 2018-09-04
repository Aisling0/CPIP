from base import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': {
        'default': dj_database_url.config('CLEARDB_DATABASE_URL'),
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SITE_URL = 'https://anamosolutions-enableireland.herokuapp.com'
ALLOWED_HOSTS.append('anamosolutions-enableireland.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
