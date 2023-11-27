from django.http import JsonResponse
from rest_framework import generics, status, viewsets
from django.utils import timezone
from comments_api.models import Comment
from comments_api.serializers import CommentSerializer
from users_api.serializers import UserSerializer, handle_image
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from django.db import transaction
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from pydub import AudioSegment
from PyPDF2 import PdfReader
from pathlib import Path
import base64

def handle_media(name, file, path, type):
    if type == "Audio":
        output_path = Path("resources/" + path + name + ".mp3")
        audio = AudioSegment.from_file(file)
        audio.export(output_path, format="mp3")
        return path + name + ".mp3"
    if type == "PDF":
        output_path = Path("resources/" + path + name + ".pdf")
        pdf = PdfReader(file)
        with open(output_path, "wb") as open_file:
            pdf.read(file)
        return path + name + ".pdf"

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def broadcast(self):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('posts', {'type': 'send_posts'})

    def create(self, request):
        try:
            with transaction.atomic():
                media = request.data.get("media")
                media_type = request.data.get("type")
                # message = request.FILES
                # return Response({'success': False, 'message': media}, status=status.HTTP_400_BAD_REQUEST)

                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                post = serializer.save()

                slz_data = serializer.data
                
                if "media" in request.data:
                    new_file_name = None
                    if media_type.startswith('image'):
                        media_type = "image"
                        new_file_name = handle_image(str(post.id) + "-" +str(timezone.now()), media, 'posts/')
                    elif media_type.startswith('audio'):
                        media_type = "audio"
                        new_file_name = handle_media(str(post.id) + "-" +str(timezone.now()), media, 'posts/', "Audio")
                    elif media_type.startswith('video'):
                        media_type = "video"
                        new_file_name = None
                    elif media_type.startswith('application'):
                        media_type = "application"
                        new_file_name = handle_media(str(post.id) + "-" +str(timezone.now()), media, 'posts/', "PDF")
                    
                    if new_file_name is not None:
                        PostMedia.objects.create(post=post, file=new_file_name, file_type=media_type)
                    
                    media_obj = PostMedia.objects.get(post=post)
                    media = PostMediaSerializer(media_obj)
                    slz_data["media"] = media.data

                comments = Comment.objects.filter(post=post)
                cmt = CommentSerializer(comments, many=True)
                slz_data["comments"] = cmt.data

                self.broadcast()
                return Response({'success': True, 'message': slz_data}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
                slz_data = slz.data
                slz_data["comments"] = cmt.data
                slz_data["media"] = media.data
                list_array.append(slz_data)
                self.broadcast()
            return Response({'success': True, 'message': list_array})

        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

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