from typing import Any
from django.db import models
from django.http import JsonResponse
from django.utils import timezone
from users_api.models import *

# class MessageContent(models.Model):
#     text = models.TextField(blank=True, null=True)
#     attached_file = models.FileField(blank=True, null=True)
    
#     def save(self, *args, **kwargs):
#         if self.text is None and self.attached_file is None:pass
#         else:
#             super().save(*args, **kwargs)


class Chat(models.Model):
    id = models.CharField(primary_key=True, max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_messages(self):
        messages = Message.objects.filter(chat_id=self.id).order_by('created_at')
        return messages

    # def save(self, id, *args, **kwargs):
    #     # Concatenate two other model's IDs to create the string ID
    #     self.id = id
    #     super().save(*args, **kwargs)
        



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    attached_file = models.FileField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
            
    class Meta:
        ordering = ('created_at',)




