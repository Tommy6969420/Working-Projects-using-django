from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
re_path(r'ws/socket/', consumers.MeetingConsumer.as_asgi()),
]