from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'message', 'media']
    
    def validate(self, data):
        message = data.get('message')
        media = data.get('media')

        if message is None and media is None:
            raise serializers.ValidationError("can't make empty post")

        return data
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    #def create(self, validated_data):
       # return super().create(self, **validated_data)
    
    