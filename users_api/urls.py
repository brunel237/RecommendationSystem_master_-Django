from django.urls import path

from .views import *

app_name = "users_api"

urlpatterns = [
    
    path('', UserViewSet.as_view({'get': 'user_list'}), name='user-list' ),
    path('<int:id>/', UserViewSet.as_view({'get': 'user_retrieve'}), name='user-retrieve'),
    path('<int:id>/update/', UserViewSet.as_view({'put': 'update'}), name='user-update'),
    path('<int:id>/delete/', UserViewSet.as_view({'delete': 'destroy'}), name='user-destroy'),
    
    
    # path('schoolelders/', SchoolElderViewSet.as_view({'get': 'list'}), name='user-schooleleder-list' ),
    # path('schoolelders/<int:id>/', SchoolElderViewSet.as_view({'get': 'retrieve'}), name='user-schooleleder-retrieve'),
    # path('schoolelders/<int:id>/update/', SchoolElderViewSet.as_view({'put': 'update'}), name='user-schooleleder-update'),
    # path('schoolelders/<int:id>/delete/', SchoolElderViewSet.as_view({'delete': 'destroy'}), name='user-schooleleder-destroy'),
    
    # path('lecturers/', LecturerViewSet.as_view({'get': 'list'}), name='user-lecturer-list' ),
    # path('lecturers/<int:id>/', LecturerViewSet.as_view({'get': 'retrieve'}), name='user-lecturer-retrieve'),
    # path('lecturers/<int:id>/update/', LecturerViewSet.as_view({'put': 'update'}), name='user-lecturer-update'),
    # path('lecturers/<int:id>/delete/', LecturerViewSet.as_view({'delete': 'destroy'}), name='user-lecturer-destroy'),
]