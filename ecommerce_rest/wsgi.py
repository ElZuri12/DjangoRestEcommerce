"""
WSGI config for ecommerce_rest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_rest.settings.local') # Aqui cambiar ya que se hizo una carpeta de settings en ves del archivo que habia antes 

application = get_wsgi_application()
