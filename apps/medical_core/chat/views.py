from django.shortcuts import render
from .models import ChatRoom, ChatMessage

def room(request, room_id):
    # جلب الغرفة أو إنشاؤها
    room_obj, created = ChatRoom.objects.get_or_create(id=room_id)
    
    # جلب جميع الرسائل السابقة لهذه الغرفة مرتبة بالأقدم أولاً
    messages = ChatMessage.objects.filter(room=room_obj).order_by('timestamp')
    
    return render(request, 'chat/room.html', {
        'room_id': room_id,
        'chat_messages': messages  # هذا المتغير يحتوي على الرسائل المحفوظة
    })