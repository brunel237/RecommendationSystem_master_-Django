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

    async def broadcast(self, action, data=None):
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            'posts',
            {
                'type': 'send.posts',
                'action': action,
                'posts' : data
            }
        )

    # async_to_sync(broadcast)()

    def create(self, request):
        # try:
        with transaction.atomic():
            media = request.data.get("media")
            media_type = request.data.get("type")
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

            async_to_sync(self.broadcast)("post-create", slz_data)
            self.broadcast("post-create", slz_data)
            return Response({'success': True, 'message': slz_data}, status=status.HTTP_201_CREATED)
        
        # except Exception as e:
        #     return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        # self.broadcast()
        return super().update(request, *args, **kwargs)

    def list(self, request):
        try:
            posts = Post.objects.all()
            list_array = []
            for post in posts:
                slz_data = get_comment_media(post)
                list_array.append(slz_data)
                # self.broadcast()
            return Response({'success': True, 'message': list_array})

        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def like(self, request, id):
        post = Post.objects.get(id=id)
        num = Like.like_post(request.user, post)
        # self.broadcast()
        return Response({"like_count": num}, status=200)

    def user_post(self, request, id):
        try:
            posts = Post.objects.filter(author_id=id)
            slz_posts = []
            for post in posts:
                slz_data = get_comment_media(post)
                slz_posts.append(slz_data)
            

            post_comment  = Comment.objects.filter(author_id=id).values_list('post_id', flat=True)
            posts = Post.objects.filter(id__in=list(post_comment))
            slz_posts_comment = []
            for post in posts:
                slz_data = get_comment_media(post)
                slz_posts_comment.append(slz_data)

            post_like = Like.objects.filter(author_id=id).values_list('post_id', flat=True)
            posts = Post.objects.filter(id__in=list(post_like))
            slz_posts_like = []
            for post in posts:
                slz_data = get_comment_media(post)
                slz_posts_like.append(slz_data)

            return Response({'success': True, 'message': {"posts":slz_posts, "related_posts":slz_posts_comment+slz_posts_like}}, status=200)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def search_posts(self, request, search=None):
        query = search
        if query:
            users = User.objects.filter(first_name__icontains=query).values_list('id', flat=True)
            users2 = User.objects.filter(last_name__icontains=query).values_list('id', flat=True)
            results = []
            posts = Post.objects.filter(author_id__in=list(users))
            posts2 = Post.objects.filter(author_id__in=list(users2))
            for p in posts:
                slz = get_comment_media(p)
                results.append(slz)
            for p in posts2:
                if p not in posts:
                    slz = get_comment_media(p)
                    results.append(slz)
        else:
            results = []
        
        return JsonResponse({'success': True, 'message': results})

def get_comment_media(post):
    slz = PostSerializer(post)
    media = PostMediaSerializer(PostMedia.objects.filter(post=post), many=True)
    cmt = CommentSerializer(Comment.objects.filter(post=post), many=True)
    slz_data = slz.data
    slz_data["comments"] = cmt.data
    slz_data["media"] = media.data
    return slz_data
