from django.contrib import admin
from .models import TelegramUser

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'chat_id', 'created_at','email')
