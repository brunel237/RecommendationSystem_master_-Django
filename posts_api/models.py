from django.db import models
from users_api.models import User
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    likes_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    

    def update(self):
        self.updated_at = timezone.now()
        self.save()


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='liked_post')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_author(self):
        return self.author
    
    def like_post(author, post):
        new_like = Like.objects.filter(author=author, post=post).first()
        if new_like:
            post.likes_count -= 1
            post.save()
            new_like.delete()
        else:
            Like.objects.create(author=author, post=post)
            post.likes_count += 1
            post.save()
        return post.likes_count
    
    class Meta:
        unique_together = ('author', 'post')

    def __str__(self):
        if self.post.message:
            return f"Liked by {self.author.username} on post {self.post.message}"
        else:
            return f"Liked by {self.author.username} on post {self.post.media}"

class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media_post')
    file = models.FileField(upload_to="posts/", blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)


