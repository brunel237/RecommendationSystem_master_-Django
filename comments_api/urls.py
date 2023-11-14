from django.urls import path
from .views import *

app_name = "comments_api"

urlpatterns = [
    path('new/', CommentViewSet.as_view({"post" : "create"}), name='comment-create'),
    path('<int:comment_id>/delete/', CommentViewSet.as_view({"delete":"destroy"}), name='comment-delete'),
    path('<int:pk>/retrieve/', CommentViewSet.as_view({"get":"retrieve"}), name='comment-retrieve'),
    path('<int:pk_post>/commentlist/',CommentViewSet.as_view({"get":"list"}), name = 'comment-list'),
]
