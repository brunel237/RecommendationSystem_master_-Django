from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserUpdateAPIView(APIView):
    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'success':False,'message':'User not found.'}, status=404)
        
        # user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success':True, 'message':serializer.data}, status=201)
        return JsonResponse({'success':False, 'message':serializer.errors}, status=400)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'



