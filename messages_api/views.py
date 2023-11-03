from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework import viewsets
from .serializers import *



class MessageViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        if not bool(request.data['sender']):
            request.data['sender'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()

        serialized_message = self.get_serializer(message)
        return Response({'success':True, 'messages':serialized_message.data})

    def get_discussions(self, request, pk=None):
        serializer = self.get_serializer(id=pk)
        serializer.is_valid(raise_exception=True)
        messages = serializer.save()
        serialized_messages = self.get_serializer(messages)
        return Response({'success':True, 'messages':serialized_messages.data})
    
    






