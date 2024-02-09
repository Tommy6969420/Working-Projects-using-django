from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/meetings/meeting/online/", consumers.ChatConsumer.as_asgi()),
]