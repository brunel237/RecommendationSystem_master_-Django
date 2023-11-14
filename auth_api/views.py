from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from users_api.serializers import *
from rest_framework.authentication import TokenAuthentication,  BasicAuthentication
from django.db import transaction
from rest_framework.views import APIView
from PIL import Image
import os
# @transaction.atomic

def handle_profile_picture(username, profile_picture):
    if bool(profile_picture):
        filename = f"{username}-{profile_picture}"
        file_path = os.path.join('resources/profile/profile_pics/', filename)
        image = Image.open(profile_picture)
        image = image.resize((200, 200))  # Adjust the size as per your requirement
        image.save(file_path)
    else:
        file_path = os.path.join('resources/profile/profile_pics/', 'profile_default.png')
    return file_path

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        with transaction.atomic():
            status = request.data.get('status')
            data = dict(request.data)
            user_fields = {}
            other_fields = {}
            for fields in User._meta.fields:
                if fields.name in data:
                    if fields.name == "password":
                        user_fields["password"] = make_password(data[fields.name])
                    else:
                        user_fields[fields.name] = data[fields.name]
            for fields in data:
                if fields not in user_fields:
                    other_fields[fields] = data[fields]
            try:
                # profile_picture = request.data.pop('profile_picture')
                try:
                    user = User.objects.create(**user_fields)
                    # user.profile_picture.save(profile_picture.name, profile_picture)
                except Exception as e:
                    return  JsonResponse({'success':False, 'message':str(e)}, status=401)
            except:
                user = User.objects.create(**user_fields)
            
            if status == "student":
                courses_attending = other_fields.pop('courses_attending')
                student = Student.objects.create(user=user, **other_fields)
                student.courses_attending.set(courses_attending)
                serialized_data = StudentSerializer(student)
            elif status == "school_elder":
                courses_attending = other_fields.pop('courses_attending')
                se = SchoolElder.objects.create(user=user, **other_fields)
                se.courses_attending.set(courses_attending)
                serialized_data = SchoolElderSerializer(se)
            else:
                lectures = other_fields.pop('lectures')
                lecturer = Lecturer.objects.create(user=user, **other_fields)
                lectures.courses_attending.set(lectures)
                serialized_data = LecturerSerializer(lecturer)
            
            token = Token.objects.create(user=user)
            return JsonResponse({'success':True, 'token':token.key, 'user':serialized_data.data}, status=201)
            
    

class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            user.is_active = True
            user.save()
            user = UserSerializer(user)
            return JsonResponse({'success':True, 'token': token.key, 'user':user.data}, status=200)
        return JsonResponse({'success':False, 'message': 'Invalid credentials'}, status=401)



class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def post(self, request, format=None):
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        Token.objects.filter(user=user.id).delete()
        return JsonResponse({'success': True, 'message': 'Successfully logged out'})

