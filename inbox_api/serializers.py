from rest_framework import serializers

from messages_api.serializers import MessageSerializer
from users_api.serializers import UserSerializer
from .models import *
from rest_framework.response import Response

class InboxSerializer(serializers.ModelSerializer):
    # owner = UserSerializer
    # guest = UserSerializer
    messages = MessageSerializer(many=True, required=False)

    class Meta:
        model = Inbox
        fields = [
            'owner',
            'guest',
            'messages',
        ]

    # def update(self, validated_data, pk=None):
    #     raise serializers.ValidationError([validated_data, pk])
    #     # msg = Message.objects.get(validated_data['messages'][0])
    #     # user = self.context['request'].user
    #     messages = validated_data.pop('messages')
    #     ib = Inbox.get_inbox(owner=validated_data['owner'], guest=messages[0]['receiver'])
    #     msg = Message.objects.get(id = messages[0]['id'])
    #     ib.messages.add(msg)
    #     discussions = ib.get_discussions()
    #     return discussions

