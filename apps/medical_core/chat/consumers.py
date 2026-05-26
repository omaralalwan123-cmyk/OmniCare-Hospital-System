import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # جلب الـ room_id من مسار الـ URL
        self.room_id = str(self.scope['url_route']['kwargs']['room_id'])
        self.room_group_name = f'chat_{self.room_id}'
        
        # جلب المستشفى الحالي الممرر تلقائياً من الـ Middleware المخصص
        self.tenant = self.scope.get("tenant")

        # السماح بالاتصال فقط إذا كان المستشفى (Tenant) معروفاً ومثبتاً
        if self.tenant:
            # الانضمام للمجموعة في الـ Redis
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            # رفض الاتصال إذا كان الطلب من نطاق غير معروف
            await self.close()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            # مغادرة المجموعة عند إغلاق الاتصال
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender_type = data.get('sender_type', 'doctor')

        # نحفظ الرسالة (تلقائياً داخل الـ Schema الخاصة بالمستشفى الحالي)
        saved_msg = await self.save_message(sender_type, message)
        
        # تنسيق الوقت ليصبح سهل القراءة
        time_str = saved_msg.timestamp.strftime('%H:%M') if saved_msg else ""

        # بث الرسالة للمجموعة
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_type': sender_type,
                'timestamp': time_str
            }
        )

    async def chat_message(self, event):
        # إرسال البيانات للمتصفح عبر الـ WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_type': event['sender_type'],
            'timestamp': event.get('timestamp', '') 
        }))

    @database_sync_to_async
    def save_message(self, sender_type, message):
        # استيراد الموديلات داخل الدالة لضمان توافق التحميل
        from .models import ChatRoom, ChatMessage
        
        try:
            # بفضل الـ Middleware، الاتصال مضبوط حالياً على الـ Schema الصحيحة تلقائياً
            room, created = ChatRoom.objects.get_or_create(id=self.room_id)
            
            new_msg = ChatMessage.objects.create(
                room=room,
                sender_type=sender_type,
                message=message
            )
            print(f"✅ Message saved successfully in schema: {self.tenant.schema_name}! ID: {new_msg.id}")
            return new_msg
        except Exception as e:
            print(f"❌ Error saving message inside schema: {e}")
            return None