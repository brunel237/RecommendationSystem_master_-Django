from django.urls import path
from .views import *

app_name = "forums_api"

urlpatterns = [
    path('', ForumViewSet.as_view({'get': 'list'}), name='get-all-forums'),
    path('new/', ForumViewSet.as_view({'post': 'create'}), name='create-forum'),
    path('retrieve/<int:pk>/', ForumViewSet.as_view({'get': 'retrieve'}), name='retrieve-forum'),
    path('update/<int:pk>/', ForumViewSet.as_view({'put': 'update'}), name='update-forum'),
    path('delete/<int:pk>/', ForumViewSet.as_view({'delete': 'destroy'}), name='destroy-forum'),
    path('<int:pk>/messages/', ForumViewSet.as_view({'get': 'get_messages'}), name='forum-get-messages'),
    path('<int:pk>/add_user/<int:pk2>/', ForumViewSet.as_view({'post': 'add_user'}), name='forum-add-user'),
    path('<int:pk>/remove_user/<int:pk2>/', ForumViewSet.as_view({'post': 'remove_user'}), name='forum-remove-user'),
    path('<int:pk>/participant_count/', ForumViewSet.as_view({'get': 'participant_count'}), name='forum-participant-count'),
]