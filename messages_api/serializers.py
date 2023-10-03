from rest_framework import serializers
from .models import *
from users_api.models import *
from users_api.serializers import *
from rest_framework.response import Response

from rest_framework import status 

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['receiver', 'text', 'attached_file']
    
    def create(self, validated_data):
        user = self.context['request'].user
        if validated_data['text'] is None and validated_data['attached_file'] is None:
            raise serializers.ValidationError
        # receiver = User.objects.get()#
        chat, _ = Chat.objects.get_or_create(id=f"{user.id}-{validated_data['receiver'].id}")
        message = Message.objects.create(sender=user, chat=chat, **validated_data)
        return message
    
    def destroy(self, validated_data, id):
        user = self.context['request'].user
        message = Message.objects.get(id=id)
        if message.sender == user.id:
            message.delete()
            return JsonResponse({'success':True})
        return JsonResponse({'success':False})
    
    def retrieve(self, pk):
        user = self.context['request'].user
        messages = Message.objects.filter(chat_id=f"{user.id}-{pk}").order_by('created_at')
        return messages

    

    
