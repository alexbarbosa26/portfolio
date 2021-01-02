from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumer
from django.core.asgi import get_asgi_application

websocket_urlPattern = [
    path('ws/polData/', consumer.DashConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlPattern
        )
    ),
})