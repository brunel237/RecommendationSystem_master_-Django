"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_asgi_application()
django.setup()

from posts_api.routing import websocket_urlpatterns as postWS
from comments_api.routing import websocket_urlpatterns as commentWS
from users_api.routing import websocket_urlpatterns as userWS
from inbox_api.routing import websocket_urlpatterns as ibWS

application = ProtocolTypeRouter(
    {
        'http': application,
        'websocket': AuthMiddlewareStack(
         URLRouter(postWS+commentWS+userWS+ibWS),
        )
    }
)
