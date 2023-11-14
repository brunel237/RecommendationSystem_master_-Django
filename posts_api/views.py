from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status, viewsets

from comments_api.models import Comment
from comments_api.serializers import CommentSerializer
from users_api.serializers import UserSerializer
from .models import Post
from .models import Like
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def broadcast():
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'posts',
        {
            'type': 'send_posts'
        }
    )


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated,]
    
    def broadcast(self):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'posts',
            {'type': 'send_posts'}
        )

    def create(self,  request):
        try:
            with transaction.atomic():
                media = request.data.pop("media")
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                post = serializer.save()
                if len(media):
                    for medium in media:
                        PostMedia.objects.create(post=post, **medium)
                self.broadcast()
                media = PostMediaSerializer(PostMedia.objects.filter(post=post), many=True)
                cmt = CommentSerializer(Comment.objects.filter(post=post), many=True)
                slz_data = dict(serializer.data)
                slz_data["comments"] = cmt.data
                slz_data["media"] = media.data
                return Response({'success': True, 'message': slz_data}, 201)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, 400)
    
    def update(self, request, *args, **kwargs):
        self.broadcast()
        return super().update(request, *args, **kwargs)

    def list(self, request):
        try:
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
                self.broadcast()
            return Response({'success': True, 'message': list_array})
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, 400)

    def like(self, request):
        post = Post.objects.get(id=request.data.get('post'))
        Like.like_post(request.user, post)
        self.broadcast()
        return Response(status=200)


# class LikeCreateView(generics.CreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = Likeserializer

#     permission_classes = [IsAuthenticated]
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         likes = serializer.save()
        
#         if likes:
#             headers = self.get_success_headers(serializer.data)
#             return JsonResponse({'success': True, 'message': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
        
#         return JsonResponse({'success': False, 'message': "This user liked the post twice, so the likes were deleted"}, status=status.HTTP_200_OK)
    
    

# class PostRetrieveView(generics.RetrieveAPIView):
#     serializer_class = PostSerializer
#     lookup_field = 'pk'
#     def get_queryset(self):
#         return Post.objects.filter(is_deleted=False)


# class PostListView(generics.ListAPIView):
#     serializer_class = PostSerializer

#     def get_queryset(self):
#         return Post.objects.filter(is_deleted=False)
    
# class LikeListView(generics.ListAPIView):
#     serializer_class = Likeserializer

#     def get_queryset(self):
#         post_id = self.kwargs['post_id']
#         return Like.objects.filter(post_id=post_id)