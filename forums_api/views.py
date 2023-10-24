from rest_framework.decorators import action

from messages_api.serializers import MessageSerializer
from .serializers import *
from .models import *
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import generics, permissions

 
class ForumViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ForumSerializer
    queryset = Forum.objects.all()
    lookup_field = 'id'
    
    def create(self, request, *args, **kwargs):
        try:
            request.data['creator'] = request.user.id
            participants = request.data.pop('participants')
            serializer = self.get_serializer(data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            forum = serializer.save()
            members = User.objects.filter(id__in=participants)
            forum.participants.add(*members)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, 400)
        return Response({'success': True, 'message': serializer.data})
    
    def destroy(self, request, pk=None):
        forum = Forum.objects.get(id=pk)
        if not bool(request.data) :
            if forum.creator == request.user:
                forum.delete_forum()
            else:
                return Response({'success': False, 'message': "Not allowed to delete this forum"}, 403)
        else :
            message = Message.objects.get(id=request.data.get('message'))
            if message.sender == request.user:
                forum.delete_message(message)
            else:
                return Response({'success': False, 'message': "Not allowed to delete this message"}, 403)
        return Response({'success': True})
        
    @action(detail=False, methods=['post'])
    def add_member(self, request, pk):
        forum = Forum.objects.get(id=pk)
        e = forum.add_member(request['member'])
        if e is True:
            return Response({'success': True, 'message': "added"}, 200)
        return Response({'success': False, 'message': e}, 400)


    @action(detail=True, methods=['post'])
    def remove_member(self, request, pk):
        forum = Forum.objects.get(id=pk)
        e = forum.remove_member(request['member'])
        if e is True:
            return Response({'success': True, 'message': "removed"}, 200)
        return Response({'success': False, 'message': e}, 400)

    @action(detail=True, methods=['get'])
    def participant_count(self, request, pk=None):
        forum = Forum.objects.get(id=pk)
        number_of_participants = forum.number_of_participants()
        return Response({'success': True, "message": number_of_participants}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def get_messages(self, request, pk=None):
        forum = Forum.objects.get(id=pk)
        discussions = forum.get_discussions()
        serializer = MessageSerializer(discussions, many=True)
        return Response({"message": serializer.data}, status=status.HTTP_200_OK)


