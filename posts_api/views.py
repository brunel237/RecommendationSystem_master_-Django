from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from .models import Post
from .models import Like
from .serializers import PostSerializer
from .serializers import Likeserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import F


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    #permission_classes = [IsAuthenticated,]

    
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success':True, 'message':serializer.data}, status=201)

    return JsonResponse({'success':False, 'message':serializer.errors}, status=400)


class PostUpdateView(APIView):
    def put(self, request, id):
        try:
            post = Post.objects.get(id=id)
        except post.DoesNotExist:
            return JsonResponse({'success':False,'message':'post not found.'}, status=404)
        
        # post = post.objects.get(id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success':True, 'message':serializer.data}, status=201)
        return JsonResponse({'success':False, 'message':serializer.errors}, status=400)


    #permission_classes = [IsAuthenticated,]

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.is_deleted = True  # Marquer le post comme supprimé
        post.save()
        return JsonResponse({'success': True, 'message': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)



class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer

    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        likes = serializer.save()
        
        if likes:
            headers = self.get_success_headers(serializer.data)
            return JsonResponse({'success': True, 'message': serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
        
        return JsonResponse({'success': False, 'message': "This user liked the post twice, so the likes were deleted"}, status=status.HTTP_200_OK)
    
    

class PostRetrieveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    lookup_field = 'pk'
    def get_queryset(self):
        return Post.objects.filter(is_deleted=False)


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(is_deleted=False)
    
class LikeListView(generics.ListAPIView):
    serializer_class = Likeserializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post_id=post_id)