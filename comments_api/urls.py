from django.urls import path
from .views import *

app_name = "comments_api"

urlpatterns = [
    path('create/', CommentViewSet.as_view({"post" : "create"}), name='comment-create'),
    path('<int:comment_id>/delete/', CommentDeleteAPIView.as_view(), name='comment-delete'),
    path('<int:pk>/retrieve/', CommentRetrieveView.as_view(), name='comment-retrieve'),
    path('<int:post_id>/commentlist/',CommentListView.as_view(), name = 'comment-list'),
]
