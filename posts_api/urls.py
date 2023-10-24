from django.urls import path
from .views import *

app_name = "post_api"

urlpatterns = [
    path('<int:id>/', PostViewSet.as_view({'get':'retrieve'}), name='post-retrieve'),
    path('', PostViewSet.as_view({'post':'create'}), name='post-create'),
    path('<int:id>/update/', PostViewSet.as_view({'put':'update'}), name='post-update'),
    path('<int:id>/delete/', PostViewSet.as_view({'delete':'destroy'}), name='post-destroy'),
]
