from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/communication/<str:tenant_slug>/', consumers.NotificationConsumer.as_asgi()),
]