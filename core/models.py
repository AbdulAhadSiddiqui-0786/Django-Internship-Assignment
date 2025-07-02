from django.db import models

class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    chat_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.username

