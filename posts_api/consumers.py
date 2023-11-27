import json
from comments_api.models import Comment

from comments_api.serializers import CommentSerializer
from .models import Post

from .serializers import *


from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions
from channels.db import database_sync_to_async


class PostConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny,]
    
    
    async def connect(self):
        self.room_group_name = 'posts'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        # await self.send(text_data=json.dumps({"message": "ok"}))  
        await self.send_posts()
        # await self.model_change.subscribe()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.save_post(data) 
        await self.send_posts()
        
    @model_observer(Post)
    async def model_change(self, message, *args, **kwargs):
        await self.send_posts()

    @database_sync_to_async
    def save_post(self, data):
        user = self.scope["user"]
        author = {"author": user}
        new_data = {**data, **author}
        serializer = PostSerializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    @database_sync_to_async
    def get_all_posts(self):
        posts = Post.objects.all()
        list_array = []
        for post in posts:
            slz = PostSerializer(post)
            media = PostMediaSerializer(PostMedia.objects.get(post=post))
            cmt = CommentSerializer(Comment.objects.filter(post=post), many=True)
            slz_data = dict(slz.data)
            slz_data["comments"] = cmt.data
            slz_data["media"] = media.data
            list_array.append(slz_data)
        return list_array
    
    async def send_posts(self):
        posts = await self.get_all_posts()  
        await self.send(text_data=json.dumps(posts))  
        # await self.send(text_data=json.dumps({"message": "ok"}))  
    
    # async def connect(self, **kwargs):
    #     await self.model_change.subscribe()
    #     await super().connect(**kwargs)


    # @model_change.serializer
    # def model_serialize(self, instance, action, **kwargs):
    #     return dict(data=PostSerializer(instance=instance).data, action=action.value)
    
    
    
    
    
    