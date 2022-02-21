"""
WSGI config for iblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from iblog.settings import settings_model


os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_model)

application = get_wsgi_application()
