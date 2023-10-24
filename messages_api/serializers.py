from rest_framework import serializers

from users_api.serializers import UserSerializer
from .models import *
from rest_framework.response import Response


class MessageSerializer(serializers.ModelSerializer):
    # receiver = UserSerializer()
    class Meta:
        model = Message
        fields = [
            'sender',
            'receiver',
            'text',
            'attached_file',
        ]
    
    def create(self, validated_data):
        if validated_data['text'] is None and validated_data['attached_file'] is None:
            raise serializers.ValidationError({"message": "Empty Message"}) 
        message = Message.objects.create( **validated_data)
        return message
    
    def destroy(self, validated_data, id):
        user = self.context['request'].user
        message = Message.objects.get(id=id)
        if message.receiver == user.id:
            message.delete()
            return Response({'success':True})
        raise serializers.ValidationError({"message": "Can just delete your message"})
    
    # def retrieve(self, validated_data, pk):
    #     user = self.context['request'].user
    #     chat = Chat.objects.get(id=f"{user.id}-{pk}")
    #     if chat is None:
    #         raise serializers.ValidationError({"message": "Chat not found"})
    #     messages = chat.get_messages()
    #     return messages

    # def get_discussions(self, id):
    #     user = self.context['request'].user
    #     chat = Chat.objects.get(id=f"{user.id}-{id}")
    #     if chat is None:
    #         raise serializers.ValidationError({"message": "Chat not found"})
    #     messages = chat.get_messages()
    #     return messages
    
    
