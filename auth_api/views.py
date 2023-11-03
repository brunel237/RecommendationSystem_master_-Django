from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from users_api.serializers import *
from rest_framework.authentication import TokenAuthentication,  BasicAuthentication
from django.db import transaction
from rest_framework.views import APIView

# @transaction.atomic


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        status = request.data.get('status')
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            request_data = dict(request.data)
            request_data["user"] = serializer.data
        except Exception as e:
            return  JsonResponse({'success':False, 'message':str(e)}, status=403)
        
        if status == "student":
            slz = StudentSerializer(data=request_data)
        elif status == "school_elder":
            slz = SchoolElderSerializer(data=request_data)
        else:
            slz = LecturerSerializer(data=request_data)
            
        if slz.is_valid():
            try:
                with transaction.atomic():
                    user = slz.save()
                    token = Token.objects.create(user=user)
                return JsonResponse({'success':True, 'token':token.key, 'user':user}, status=201)
            except Exception as e:
                return  JsonResponse({'success':False, 'message':str(e)}, status=401)
        else:
            return JsonResponse({'success':False, 'message':slz.errors}, status=400)
    

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

