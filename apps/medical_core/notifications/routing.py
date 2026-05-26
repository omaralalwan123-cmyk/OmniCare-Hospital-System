from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # مسار نظيف لفتح اتصال الإشعارات الفورية
    path('ws/notifications/', consumers.NotificationConsumer.as_asgi()),
]