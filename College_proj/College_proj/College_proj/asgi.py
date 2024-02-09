"""
ASGI config for College_proj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import meetings.routing
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'College_proj.settings')
application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(meetings.routing.websocket_urlpatterns
        )),
    "http":get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})