"""
ASGI config for ecommerce_rest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_rest.settings.local') # Aqui cambiar ya que se hizo una carpeta de settings en ves del archivo que habia antes 
application = get_asgi_application()
