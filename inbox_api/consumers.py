from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.permissions import IsAuthenticated
from channels.db import database_sync_to_async
from inbox_api.serializers import *
import json

class InboxConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        recipient_id = self.scope['url_route']['kwargs']['recipient_id']
        sender_id = self.scope['user'].id

        if not await self.is_valid_user(sender_id) or not await self.is_valid_user(recipient_id):
            await self.close()
            return

        self.room_name = self.get_private_chat_room_name(sender_id, recipient_id)
        self.room_group_name = f'private_chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        message = json_data['message']
        sender_id = json_data['sender_id']
        receiver_id = json_data['receiver_id']
        
        data = {"sender_id": sender_id, "receiver_id": receiver_id, "text": message}

        msg = await self.save_message(data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'chat.message', 'message': msg}
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))

    @database_sync_to_async
    def is_valid_user(self, user_id):
        return User.objects.filter(id=user_id).exists()

    @staticmethod
    def get_private_chat_room_name(sender_id, recipient_id):
        return f'{min(int(sender_id), int(recipient_id))}_{max(int(sender_id), int(recipient_id))}'

    @database_sync_to_async
    def save_message(self, message):
        try:
            with transaction.atomic():
                msg = Message.objects.create(**message)
                ibs = Inbox.objects.filter(owner_id=message["sender_id"], guest_id=message["receiver_id"])
                if len(list(ibs)):
                    for ib in ibs:
                        ib.messages.add(msg)
                else:
                    ibs = Inbox.objects.filter(owner_id=message["receiver_id"], guest_id=message["sender_id"])
                    if len(list(ibs)):
                        for ib in ibs:
                            ib.messages.add(msg)
                    else:
                        ib = Inbox.objects.create(owner_id=message["sender_id"], guest_id=message["receiver_id"])
                        ib.messages.add(msg)
                slz = MessageSerializer(msg)
                return {"message": slz.data}
        except Exception as e:
            return e
