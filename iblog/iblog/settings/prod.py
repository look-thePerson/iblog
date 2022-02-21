import os

from iblog.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iblog',
        'USER': 'iblog',
        'PASSWORD': os.getenv('IBLOG_DATABASE_PASSWORD')
    }
}
