from django.db import models
from users_api.models import User
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    media = models.FileField( blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)

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


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_author_id(self):
        return self.author_id
    

    class Meta:
        unique_together = ('author', 'post')


    def __str__(self):
        return f"Like by {self.author.username} on post {self.post.id}"




