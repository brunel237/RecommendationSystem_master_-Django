from channels.generic.websocket import AsyncWebsocketConsumer

class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'users'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
   
    async def receive(self, text_data):
        # Handle incoming WebSocket messages
        pass