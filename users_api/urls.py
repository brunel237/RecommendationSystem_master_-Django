from django.urls import path

from .views import *

app_name = "users_api"

urlpatterns = [
    path('users/<int:id>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('users/<int:id>/update', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:id>/destroy/', UserDestroyAPIView.as_view(), name='user-destroy'),
]