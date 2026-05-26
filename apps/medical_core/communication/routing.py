from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # مسار ديناميكي يستقبل اسم المستشفى لفرز وتأمين الاتصالات
    re_path(r'ws/communication/(?P<tenant_slug>[\w-]+)/$', consumers.NotificationConsumer.as_asgi()),
]