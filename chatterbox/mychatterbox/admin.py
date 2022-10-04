from django.contrib import admin
from .models import Profile, Friend, ChatMessage

# Register your models here.

admin.site.register(Profile)
admin.site.register(Friend)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('body', 'msg_sender', 'msg_receiver', 'received_at')
