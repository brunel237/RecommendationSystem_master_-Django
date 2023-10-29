from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import F,Value
from posts_api.models import Post


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def create(self, request, pk=None):
    
        serializer = CommentSerializer(data=request.data,context= {'request':request})
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save()
            return Response({"success": True}, status=200)
        return Response({"success":False}, status= 400)


    

class CommentDeleteAPIView(APIView):
    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response({"message": "Comment not found"}, status=404)

        post = Post.objects.get(id = comment.post.id) 
        Post.objects.filter(id=post.id).update(comment_count = F('comment_count')- Value(1))
        comment.is_deleted = True
        comment.save()
        return Response({"success": True}, status=200)




class CommentRetrieveView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    def get_queryset(self):
        return Comment.objects.filter(is_deleted=False)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id, is_deleted=False)