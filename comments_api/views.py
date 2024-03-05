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
    permission_classes = [IsAuthenticated,]
    lookup_field = "id"

    def create(self, request):
        try:
            serializer = CommentSerializer(data=request.data,context= {'request':request})
            
            if serializer.is_valid(raise_exception=True):
                comment = serializer.save()
                return Response({"success": True, "message":serializer.data}, status=200)
        except Exception as e:
            return Response({"success":False, "message":str(e)}, status= 400)
        
    def destroy(self, request, comment_id=None):
        comment = Comment.objects.get(id=comment_id)
        if comment:
            Comment.delete_comment(comment)
            return Response(status=200)
        else:
            return Response(status=404)

