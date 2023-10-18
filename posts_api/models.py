from django.db import models
from users_api.models import User
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    media = models.FileField( blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        
    def restore(self):
        self.deleted_at = None
        self.save()
        
    def update(self):
        self.updated_at = timezone.now()
        self.save()

    def save(self,*args,**kwargs):
        if self.deleted_at is None:
            super().save(*args, **kwargs)
        else:
            pass




