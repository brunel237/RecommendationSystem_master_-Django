from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from users_api.serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from django.db import transaction
from rest_framework.views import APIView

# @transaction.atomic


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication)
    
    # @transaction.atomic
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    user = serializer.save()
                    token = Token.objects.create(user=user)
                return JsonResponse({'success':True, 'token':token.key}, status=201)
            except Exception as e:
                # return  Exception
                return  JsonResponse({'success':False, 'message':str(e)}, status=400)
        else:
            return JsonResponse({'success':False, 'message':serializer.errors}, status=400)
    

class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'success':True, 'token': token.key}, status=200)
        return JsonResponse({'success':False, 'detail': 'Invalid credentials'}, status=401)



# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([permissions.IsAuthenticated])


# @csrf_exempt
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def post(self, request, format=None):
        logout(request)
        Token.objects.filter(user=request.user.id).delete()
        return JsonResponse({'success': True, 'message': 'Successfully logged out'})
        #return JsonResponse({'success': False, 'message': 'User not authenticated'})

