from django.db import models
from django.utils import timezone
from users_api.models import *
from posts_api.models import *


# "token": "39dfb9065634804f30fe92748ccff5b064672f7b"
#"token": "a4c20c4e13a793ee8604b9948b7a2a754a06408e"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author.username}"
    
    
    def delete(self):
        self.is_deleted = True
        self.save()
        
    def save(self, *args, **kwargs):
        is_new_comment = self.pk is None  # Vérifie si le commentaire est nouvellement créé
        super().save(*args, **kwargs)
        
        if is_new_comment:
            self.post.comment_count = Comment.objects.filter(post=self.post, is_deleted=False).count()
            self.post.save()
    
    
    
    def get_author_id(self):
        return self.author_id
    

