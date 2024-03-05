from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/inbox/(?P<recipient_id>\d+)/', consumers.InboxConsumer.as_asgi()),
]