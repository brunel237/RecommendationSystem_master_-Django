from django.urls import path

from .views import *

app_name = "users_api"

urlpatterns = [
    
    path('', UserViewSet.as_view({'get': 'user_list'}), name='user-list' ),
    path('<int:id>/', UserViewSet.as_view({'get': 'user_retrieve'}), name='user-retrieve'),
    path('<int:id>/update/', UserViewSet.as_view({'put': 'update'}), name='user-update'),
    path('<int:id>/delete/', UserViewSet.as_view({'delete': 'destroy'}), name='user-destroy'),
    path('follow/<int:id>/', UserViewSet.as_view({'post': 'follow'}), name='user-follow'),
    path('search/<str:search>/', UserViewSet.as_view({'get': 'search_user'}), name='search-user'),
    
]
