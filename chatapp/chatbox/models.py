from django.db import models

# Create your models here.

class ChatInfo(models.Model):
    username = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
