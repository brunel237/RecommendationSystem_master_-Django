from django.urls import path
from .views import *

app_name = "faculties_api"

urlpatterns = [
    path('', FacultyViewSet.as_view({'get' : 'list'}), name="faculty-list"),
    path('new/', FacultyViewSet.as_view({'post' : 'create'}), name="faculty-create"),
    path('<int:id>/', FacultyViewSet.as_view({'get' : 'retrieve'}), name="faculty-retrieve"),
    path('<int:id>/update/', FacultyViewSet.as_view({'put' : 'update'}), name="faculty-update"),
    path('<int:id>/delete/', FacultyViewSet.as_view({'delete' : 'destroy'}), name="faculty-destroy"),
]