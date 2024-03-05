from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.permissions import IsAuthenticated
from channels.db import database_sync_to_async
from comments_api.serializers import *
from users_api.serializers import *
import json

class CommentConsumer(AsyncWebsocketConsumer):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    groups = ['comments']

    async def connect(self):
        self.group_name = 'comments'
        await self.accept()

    async def disconnect(self, close_code):
        pass
   
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        post_id = data.get('post_id')
        user_id = data.get('user_id')
        content = data.get('content')
        comment = await self.comment_posts(content, user_id, post_id)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send.post',
                'comment': comment
            }
        )
        
 
    @database_sync_to_async
    def comment_posts(self, content, user_id, post_id):
        if not len(content):
            return {'error': "Can't save empty post"}
        post = Post.objects.get(id=post_id)
        author = User.objects.get(id=user_id)
        comment = Comment.make_comment(post, author, content)
        serializer = CommentSerializer(comment)
        return serializer.data
        

    async def send_post(self, event):
        comment =  event['comment']
        await self.send(text_data=json.dumps(comment)) 
        pass