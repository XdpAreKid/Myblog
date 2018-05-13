from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# INSTALLED_APPS += ["debug_toolbar", ]

ALLOWED_HOSTS = ['*', ]


PAGE_SIZE = 2

SECRET_KEY = "you secret key"
