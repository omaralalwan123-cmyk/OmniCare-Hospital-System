from django.urls import path
from . import views

urlpatterns = [
    path('chat/<uuid:room_id>/', views.room, name='room'),
]