from django.urls import path
from .views import *

app_name = "recommendations_api"

urlpatterns = [
    path('<int:id>/', RecommendationViewSet.as_view({'get':'recommendation_list'}), name='recommendation-list'),
    # path('posts/<int:id>', RecommendationViewSet.as_view({'get':'posts_list'}), name='posts-recommend-list'),
]
