from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from users_api.serializers import *
from rest_framework.authentication import TokenAuthentication,  BasicAuthentication
from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from recommendations_api.models import *


def get_recommendations(user_id):
    recommended_users_data = recommend_users(user_id)
    return recommended_users_data


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
                    user_fields[fields.name] = request.data.get(fields.name)
            for fields in data:
                if fields not in user_fields and  fields != 'csrfmiddlewaretoken':
                    other_fields[fields] = request.data.get(fields)
                    
            try:
                user_serializer = self.get_serializer(data=user_fields)
                user_serializer.is_valid(raise_exception=True)
                user = user_serializer.save()
            except Exception as e:
                return  JsonResponse({'success':False, 'message':str(e)}, status=400)

            if status == "student":
                if "courses_attending" in other_fields:
                    courses_attending = other_fields.pop('courses_attending')
                student = Student.objects.create(user=user, **other_fields)
                if "courses_attending" in other_fields:
                    student.courses_attending.set(courses_attending)
                serialized_data = StudentSerializer(student)
            elif status == "school_elder":
                if "courses_attending" in other_fields:
                    courses_attending = other_fields.pop('courses_attending')
                se = SchoolElder.objects.create(user=user, **other_fields)
                if "courses_attending" in other_fields:
                    se.courses_attending.set(courses_attending)
                serialized_data = SchoolElderSerializer(se)
            else:
                if "lectures" in other_fields:
                    lectures = other_fields.pop('lectures')
                lecturer = Lecturer.objects.create(user=user, **other_fields)
                if "lectures" in other_fields:
                    lecturer.lectures.set(lectures)
                serialized_data = LecturerSerializer(lecturer)
            
            token = Token.objects.create(user=user)
            get_recommendations(user.id)

            return JsonResponse({'success':True, 'token': token.key, 'user':serialized_data.data}, status=200)

            


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
            if user.status == "student":
                slz_data = StudentSerializer(Student.objects.get(user=user))
            elif user.status == "school_elder":
                slz_data = SchoolElderSerializer(SchoolElder.objects.get(user=user))
            else:
                slz_data = LecturerSerializer(Lecturer.objects.get(user=user))
            
            get_recommendations(user.id)

            return JsonResponse({'success':True, 'token': token.key, 'user':slz_data.data}, status=200)
        return JsonResponse({'success':False, 'message': 'Invalid credentials'}, status=400)



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

