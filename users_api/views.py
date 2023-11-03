import json
from django.http import JsonResponse
from rest_framework import generics, viewsets, permissions
from rest_framework.views import APIView
# from django.contrib.auth

from .models import *
from .serializers import *



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    
    def retrieve(self, request, id):
        school_elder = SchoolElder.objects.get(pk=id)
        serializer = SchoolElderSerializer(school_elder)
        serialized_data = serializer.data
        return JsonResponse(serialized_data)
    
    def user_list(self,request=None, validated_data=None):
        users = User.objects.all()
        resp = []
        for user in users:
            try:
                val = self.user_retrieve(None, user.id)
                val = json.loads(val.content)
                val = val["message"]
                resp.append(val)
            except Exception as e:
                continue
        return JsonResponse(resp, safe=False)
    
    def user_retrieve(self,request=None, id=None):
        user = User.objects.get(id=id)
        if user is not None :
            user = user.get_user()
            if user.user.status=="student":
                serialized_message = StudentSerializer(user)
            elif user.user.status=="school_elder":
                serialized_message = SchoolElderSerializer(user)
            else:
                serialized_message = LecturerSerializer(user)
            return JsonResponse({"success":True, "message":serialized_message.data})
        return JsonResponse({"success":False, "message":"User not Found"})
    
    def update(self, request, id):
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'User not found'}, status=404)

        if request.user != user or request.user.is_superuser:
            return JsonResponse({'success':False, 'message': 'Action Denied !'}, status=405)

        serializer = self.get_serializer(data=request.data, instance=user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if user.status == "student":
            user_type = Student.objects.get(user=user)
            slz = StudentSerializer(instance=user_type, data=request.data, partial=True)
        elif user.status == "school_elder":
            user_type = SchoolElder.objects.get(user=user)
            slz = SchoolElderSerializer(instance=user_type, data=request.data, partial=True)
        else:
            user_type = Lecturer.objects.get(user=user)
            slz = LecturerSerializer(instance=user_type, data=request.data, partial=True)
        
        slz.is_valid(raise_exception=True)
        slz.save()
        
        serializer.data["user_type"] = slz.data
        
        return JsonResponse({'success':True, 'message':serializer.data})
    
    def destroy(self, request, id, *args, **kwargs):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return JsonResponse({'success':False, 'message': 'User not found'}, status=404)

        if not request.user.is_superuser and request.user != user:
            return JsonResponse({'success':False, 'message': 'Action Denied !'}, status=405)

        return super().destroy(request, *args, **kwargs)

    def profile(self, request, pk=None):
        pass
    
