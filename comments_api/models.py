from django.db import models
from django.utils import timezone
from users_api.models import User
from posts_api.models import Post
from django.db import transaction

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commented_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Commented by {self.author.username}"
    
    def make_comment(post, author, content):
        comment = Comment.objects.create(author=author, content=content, post=post)
        post.comment_count += 1
        post.save()
        return comment
    
    def delete_comment(comment):
        with transaction.atomic():
            post = Post.objects.get(id=comment.post.id)
            post.comment_count -= 1
            comment.delete()
            post.save()

    # def save(self, *args, **kwargs):
    #     is_new_comment = self.pk is None  # Vérifie si le commentaire est nouvellement créé
    #     super().save(*args, **kwargs)
        
    #     if is_new_comment:
    #         self.post.comment_count = Comment.objects.filter(post=self.post).count()
    #         self.post.save()
    

    def get_author(self):
        return self.author
    

