from django.db import models

# Create your models here.
from django.db import models

class ChatMessage(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input

