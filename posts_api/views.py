from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


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





