from rest_framework import generics, permissions
from rest_framework import viewsets
from .serializers import *


class InboxViewSet(viewsets.ModelViewSet):
    permission_classes =[permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = InboxSerializer
    queryset = Inbox.objects.all()
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            ib = Inbox.objects.get(id=pk)
            if ib.owner != request.user and ib.hidden:
                return Response({'success': False, 'message': {}}, 404)
            messages = ib.get_visible_messages(request.user)
            serialized = MessageSerializer(messages, many=True)
            output_data = {"owner": ib.owner.id, "guest":ib.guest.id, "messages":serialized.data}
            return Response({'success': True, 'message': output_data})
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, 400)
    
    def update(self, request, pk=None):
        try:
            with transaction.atomic():
                slz = MessageSerializer(data = request.data, partial=True)
                slz.is_valid(raise_exception=True)
                msg = slz.save()
                
                inbox = Inbox.get_inbox(request.user, msg.receiver)
                inbox.messages.add(msg)
                
                serializer = InboxSerializer(instance=inbox, partial=True)

        except Exception as e:
            return Response({'success': False, 'message': str(e)}, 400)
        return Response({'success': True, 'message': serializer.data})
    
    def delete(self, request, pk=None):
        ib = Inbox.objects.get(id=pk)
        if not bool(request.data) :
            if ib.owner == request.user:
                messages = ib.messages.all()
                messages.delete()
                ib.delete()
            else:
                ib.hide_inbox()
        else:
            message = Message.objects.get(id=request.data.get('message'))
            if message.receiver == request.user:
                ib.hide_message(message)
            else:
                e = ib.delete_message(message)
                if e is not True:
                    return Response({'success': False, 'message': e})
        return Response({'success': True})

    def list(self, request):
        user = request.user
        inboxes = Inbox.objects.filter(owner=user)
        serialized = InboxSerializer(inboxes, many=True)
        inboxes2 = Inbox.objects.filter(guest=user)
        serialized2 = InboxSerializer(inboxes2, many=True)
        return Response({'success': True, 'message': serialized.data+serialized2.data})

