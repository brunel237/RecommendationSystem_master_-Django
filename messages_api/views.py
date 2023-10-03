from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import *
from .models import *



class MessageViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()

        serialized_message = self.get_serializer(message)
        return Response(serialized_message.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # messages = serializer.save()
        user = self.request.user
        messages = Message.objects.filter(chat_id=f"{user.id}-{pk}").order_by('created_at')
        # return messages
        # serialized_messages = self.get_serializer(messages)
        return Response({'success':True, 'messages':str(messages)}, status=status.HTTP_201_CREATED)






