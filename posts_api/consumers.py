import json
from comments_api.models import Comment

from comments_api.serializers import CommentSerializer
from .models import *

from .serializers import PostSerializer, PostMediaSerializer
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.permissions import IsAuthenticated
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions
from channels.db import database_sync_to_async
from rest_framework.request import Request
from django.http import HttpRequest


class PostConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]
    
    groups = ['posts']

    
    async def connect(self):
        self.room_group_name = 'posts'
        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
        await self.accept()
        posts_data = await self.get_all_posts()
        data = {"action": "post-list", "posts": posts_data}
        await self.send_posts({"data":data})


    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data['action'] == "post-create":
            slz_post = await self.save_post(data['posts']) 
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type" : "send.posts",
                    "data" : {"action": "post-create", "posts": slz_post}
                }
            )
        pass
        
    @model_observer(Post)
    async def model_change(self, message, *args, **kwargs):
        await self.send_posts()

    @database_sync_to_async
    def save_post(self, post_data):
        post = Post.objects.create(**post_data)
        slz = PostSerializer(post)
        media = PostMediaSerializer(PostMedia.objects.filter(post=post), many=True)
        cmt = CommentSerializer(Comment.objects.filter(post=post), many=True)
        slz_data = dict(slz.data)
        slz_data["comments"] = cmt.data
        slz_data["media"] = media.data
        return slz_data

    @database_sync_to_async
    def get_all_posts(self):
        posts = Post.objects.all()
        list_array = []
        for post in posts:
            slz = PostSerializer(post)
            media = PostMediaSerializer(PostMedia.objects.filter(post=post), many=True)
            cmt = CommentSerializer(Comment.objects.filter(post=post), many=True)
            slz_data = dict(slz.data)
            slz_data["comments"] = cmt.data
            slz_data["media"] = media.data
            list_array.append(slz_data)
        return list_array
    
    async def send_posts(self, event):
        this_data = event["data"]
        await self.send(text_data=json.dumps(this_data))
        # await self.send(text_data=json.dumps({"message": "ok"}))
    
    # async def connect(self, **kwargs):
    #     await self.model_change.subscribe()
    #     await super().connect(**kwargs)


    # @model_change.serializer
    # def model_serialize(self, instance, action, **kwargs):
    #     return dict(data=PostSerializer(instance=instance).data, action=action.value)

class LikeConsumer(AsyncWebsocketConsumer):
    permission_classes = [permissions.AllowAny,]
    groups = ['likes']

    async def connect(self):
        self.group_name = 'likes'
        # await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # await self.channel_layer.group_discard(self.group_name, self.channel_name)
        pass
   
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        post_id = data.get('post_id')
        user_id = data.get('user_id')
        post_data = await self.like_posts(user_id, post_id)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send.likes',
                'likes': post_data
            }
        )
        

    @database_sync_to_async
    def like_posts(self,user_id, post_id):
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        likes_count = Like.like_post(user, post)
        return {'likes_count': likes_count, 'post_id': post_id}
        

    async def send_likes(self, event):
        likes =  event['likes']
        await self.send(text_data=json.dumps(likes)) 
        pass