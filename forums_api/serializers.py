from rest_framework import serializers
from .models import *
from users_api.serializers import *
from rest_framework.response import Response
from rest_framework import status

 
class ForumSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, required=False)
    
    class Meta:
        model = Forum
        fields = ['name', 'purpose','creator', 'participants',]
    
    # def create(self, validated_data):
    #     participants = validated_data.pop('participants')
    #     forum = Forum.objects.create(**validated_data)
    #     for user in participants:
    #         forum.participants.add(user)
    #     return forum
    
