from rest_framework import serializers
from .models import Post
from .models import Like
from django.db.models import F

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['author', 'message', 'media','created_at','comment_count','likes_count']

    def get_likes_count(self, obj):
        return obj.likes_count
    def get_comment_count(self,obj):
        return obj.comment_count

    
    def validate(self, data):
        message = data.get('message')
        media = data.get('media')
    
        if message is None and media is None:
            raise serializers.ValidationError("can't make empty post")

        return data
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

class Likeserializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='get_user_id')  # Champ en lecture seule
    
    class Meta:
        model = Like
        fields = ['author', 'post', 'created_at',]

    def get_likes_count(self,instance):
        return instance.post.likes_count
    
    def validate(self, data):
        author = data.get('author')
        post = data.get('post')

        return data
    
    def create(self, validated_data):
        post = validated_data['post']
        author = self.context['request'].user
        
        existing_like = Like.objects.filter(author=author, post=post).first()
        if existing_like:
            existing_like.delete()
            post.likes_count = F('likes_count') - 1  # Décrémente like_count du Post
            post.save()
            raise serializers.ValidationError("This post has already been liked by this user.")
        else:
            like = Like.objects.create(author=author, **validated_data)
            post.likes_count = F('likes_count')+ 1 # Incrémente like_count du Post
        
        post.save()
        return like
    
    
    
    
    