from django.urls import path
from .views import *

app_name = "inbox_api"


urlpatterns = [
    path('', InboxViewSet.as_view({'put': 'update'}), name='send-message-inbox'),
    path('<int:pk>/', InboxViewSet.as_view({'get': 'retrieve'}), name='list-message-inbox'),
    path('<int:pk>/delete/', InboxViewSet.as_view({'delete': 'delete'}), name='delete-message-inbox'),
    path('discussions/', InboxViewSet.as_view({'get': 'list'}), name='delete-message-inbox'),
]