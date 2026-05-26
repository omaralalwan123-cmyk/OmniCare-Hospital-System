import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get("user")
        self.tenant = self.scope.get("tenant")

        # السماح بالاتصال طالما أن المستشفى (Tenant) معروف ومحدد
        if self.tenant:
            self.groups_list = []

            # 1. الانضمام للمجموعة العامة للمستشفى (لكل المتصلين: زوار ومستخدمين)
            self.global_group = f"notify_{self.tenant.schema_name}_broadcast"
            await self.channel_layer.group_add(self.global_group, self.channel_name)
            self.groups_list.append(self.global_group)

            # 2. إذا كان المستخدم مسجلاً دخوله، نضمه أيضاً لمجموعته الخاصة الفردية
            if self.user and self.user.is_authenticated:
                self.user_group = f"notify_{self.tenant.schema_name}_{self.user.id}"
                await self.channel_layer.group_add(self.user_group, self.channel_name)
                self.groups_list.append(self.user_group)

            await self.accept()
        else:
            # رفض الاتصال تماماً إذا لم يتم التعرف على المستشفى من الـ URL
            await self.close()

    async def disconnect(self, close_code):
        # تنظيف الاتصال من كل المجموعات التي انضم إليها المتصفح عند الإغلاق
        if hasattr(self, 'groups_list'):
            for group in self.groups_list:
                await self.channel_layer.group_discard(group, self.channel_name)

    # استقبال الإشعار (العام أو الخاص) وبثه فوراً للمتصفح عبر الـ WebSocket
    async def send_notification(self, event):
        notification_data = event["data"]
        await self.send(text_data=json.dumps({
            "type": "notification",
            "payload": notification_data
        }))