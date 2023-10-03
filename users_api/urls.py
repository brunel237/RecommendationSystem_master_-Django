from django.urls import path

from .views import *

app_name = "users_api"

urlpatterns = [
    path('<int:id>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('update/<int:id>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:id>/', UserDestroyAPIView.as_view(), name='user-destroy'),
]