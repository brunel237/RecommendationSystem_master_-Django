from rest_framework import serializers
from .models import *
from users_api.serializers import *
from rest_framework.response import Response
from rest_framework import status

 
class ForumSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Forum
        fields = ['name', 'purpose', 'participants',]
    
    def create(self, validated_data):
        user = self.context['request'].user
        if (user.is_student or user.is_teacher ) :
            chat, _ = Chat.objects.get_or_create(id=f"{user.id}-{validated_data['name']}")
            forum = Forum.objects.create(chat=chat, creator=user, **validated_data)
            # serialized_forum = self.Meta.model(forum).data
            return forum
        else :
            raise serializers.ValidationError({'message': 'Not Authorized'})
        
        
    