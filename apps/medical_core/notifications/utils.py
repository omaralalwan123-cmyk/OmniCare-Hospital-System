import asyncio
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_global_notification(tenant_schema, title, message):
    channel_layer = get_channel_layer()
    group_name = f"notify_{tenant_schema}_broadcast"
    
    # الصياغة المطابقة تماماً لـ Consumer الخاص بك
    payload = {
        "type": "send_notification",  # تطابق اسم الدالة async def send_notification
        "data": {                      # تطابق المفتاح event["data"]
            "title": title,
            "message": message
        }
    }
    
    try:
        # الإرسال من السياق العادي (كالـ Shell)
        async_to_sync(channel_layer.group_send)(group_name, payload)
    except RuntimeError:
        # الإرسال الآمن من سياق Celery المعزول تزامناً
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(channel_layer.group_send)(group_name, payload)
        loop.close()