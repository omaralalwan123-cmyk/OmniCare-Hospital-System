import uuid
from django.db import models

class ChatRoom(models.Model):
    # استخدام UUID كمفتاح أساسي بدلاً من ID الرقمي
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class ChatMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=20) # 'doctor' or 'patient'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp'] # الاعتماد على الوقت في الترتيب وليس الـ ID