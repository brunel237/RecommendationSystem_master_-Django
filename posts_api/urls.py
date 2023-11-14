from django.urls import path
from .views import *

app_name = "posts_api"

urlpatterns = [
    path('<int:id>/', PostViewSet.as_view({'get':'retrieve'}), name='post-retrieve'),
    path('', PostViewSet.as_view({'get':'list'}), name='post-list'),
    path('new/', PostViewSet.as_view({'post':'create'}), name='post-create'),
    path('<int:id>/update/', PostViewSet.as_view({'put':'update'}), name='post-update'),
    path('<int:id>/delete/', PostViewSet.as_view({'delete':'destroy'}), name='post-destroy'),
    path('like/', PostViewSet.as_view({'post':'like'}), name='post-like'),
]
