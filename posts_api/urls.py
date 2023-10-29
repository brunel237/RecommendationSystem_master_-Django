from django.urls import path
from .views import *

app_name = "post_api"

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post-destroy'),
    path('like/', LikeCreateView.as_view(), name='post-like'),
    path('<int:pk>/retrieve/', PostRetrieveView.as_view(), name='post-retrieve'),
    path('postlist/',PostListView.as_view(), name = 'post-list'),
    path('<int:post_id>/likelist/',LikeListView.as_view(), name = 'like-list'),
]
