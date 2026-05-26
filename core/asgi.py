import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.middleware import BaseMiddleware
from django_tenants.utils import schema_context

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.init()

# تهيئة تطبيق ASGI العادي للـ HTTP
django_asgi_app = get_asgi_application()

# استيراد مسارات الـ WebSocket بعد تهيئة دجانجو
from apps.medical_core.communication.routing import websocket_urlpatterns

# 🧠 ميدل وير ذكي لفرز قاعدة البيانات للمستأجرين تلقائياً دون استدعاء موديلات
class ChannelsTenantMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        path = scope.get("path", "")
        parts = [p for p in path.split("/") if p]
        
        # الرابط: ws/communication/shifa/ -> الجزء الثالث (الفهرس 2) هو الـ tenant_slug
        tenant_slug = parts[2] if len(parts) >= 3 else None
        
        if tenant_slug:
            # عزل بيئة قاعدة البيانات فوراً لتشغيل الـ AuthMiddlewareStack بأمان
            with schema_context(tenant_slug):
                return await super().__call__(scope, receive, send)
        
        return await super().__call__(scope, receive, send)

# خريطة البروتوكولات الأساسية للمشروع
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": ChannelsTenantMiddleware(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    ),
})