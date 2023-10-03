from rest_framework.decorators import action
from .serializers import *
from .models import *
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import generics, permissions

 
class ForumViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ForumSerializer
    queryset = Forum.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        forum = serializer.save()

        serialized_forum = self.get_serializer(forum)
        return Response(serialized_forum.data, status=status.HTTP_201_CREATED)

    # @action(detail=False, methods=['post'])
    def add_user(self, request, pk, pk2):
        forum = Forum.objects.get(id=pk)
        user_id = request.data.get('user_id')
        user = User.objects.get(id=pk2)
        forum.participants.add(user)
        return JsonResponse({'success':True, 'message': 'User added to the forum.'})

    # @action(detail=True, methods=['post'])
    def remove_user(self, request, pk, pk2):
        forum = Forum.objects.get(id=pk)
        user_id = request.data.get('user_id')
        user = User.objects.get(id=pk2)
        forum.participants.remove(user)
        return JsonResponse({'success':True, 'message': 'User removed from the forum.'})

    @action(detail=True, methods=['get'])
    def participant_count(self, request, pk=None):
        forum = self.get_object()
        count = forum.participants.count()
        return JsonResponse({'success':True, 'participant_count': count})

    @action(detail=True, methods=['get'])
    def get_messages(self, request, pk=None):
        forum = Forum.objects.get(id=pk)
        messages = Message.objects.filter(chat=forum.chat).order_by('created_at')
        return JsonResponse({'success':True, 'message': str(messages)})


