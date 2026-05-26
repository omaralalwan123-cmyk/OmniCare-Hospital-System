from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # مسار الشات فقط! لا تضع هنا أي مسار يخص الإشعارات
    path('ws/chat/<uuid:room_id>/', consumers.ChatConsumer.as_asgi()),
]