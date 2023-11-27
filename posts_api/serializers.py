from rest_framework import serializers
from .models import *
from django.db.models import F
from users_api.serializers import *

    
class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    author  = UserSerializer(required=False)
    
    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.likes_count
    
    def get_comment_count(self,obj):
        return obj.comment_count

    
    # def validate(self, data):
    #     message = data.get('message')
    #     media = data.get('media')
    
    #     if message is None and media is None:
    #         raise serializers.ValidationError({"message": "can't make empty post"})

    #     return data

    def create(self, validated_data):
        message = validated_data.get("message")
        media = validated_data.get("media")
        if ((message and len(message)) or (media)):
            return Post.objects.create(author=self.context['request'].user, message=message)
        else:
            raise serializers.ValidationError({"message":str(message), "media":str(media)})

class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = '__all__'

    