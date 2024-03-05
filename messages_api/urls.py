from django.urls import path
from .views import *

app_name = "messages_api"


urlpatterns = [
    path('', MessageViewset.as_view({'post': 'create'}), name='send-user-message'),
    path('<int:pk>/retrieve', MessageViewset.as_view({'get': 'get_discussions'}), name='get-user-message'),
    path('<int:pk>/delete', MessageViewset.as_view({'delete': 'destroy'}), name='destroy-user-message'),
]