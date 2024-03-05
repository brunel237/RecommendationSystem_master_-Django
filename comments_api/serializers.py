from rest_framework import serializers
from django.db.models import F
from posts_api.models import Post
from users_api.serializers import UserSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)
    
    class Meta:
        model = Comment
        fields = '__all__'

    
    def validate(self, data):
        content = data.get('content')
        if content is None :
            raise serializers.ValidationError("can't make empty comment")
        return data


    def create(self, validated_data):
        post = Post.objects.get(id=validated_data['post'].id)
        author = self.context['request'].user
        comment = Comment.make_comment(post=post, author=author,  content=validated_data['content'])
        return comment
    
    
    
    
    