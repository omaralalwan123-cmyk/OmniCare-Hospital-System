from django.contrib import admin
from .models import ChatRoom, ChatMessage

class MessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 1
    readonly_fields = ('timestamp',)

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at') 
    inlines = [MessageInline]

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'sender_type', 'message', 'timestamp')
    list_filter = ('sender_type', 'room')