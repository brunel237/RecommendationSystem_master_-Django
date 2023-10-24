from django.urls import path
from .views import *

app_name = "departments_api"

urlpatterns = [
    path('', DepartmentViewSet.as_view({'get' : 'list'}), name="department-list"),
    path('new/', DepartmentViewSet.as_view({'post' : 'create'}), name="department-create"),
    path('<int:id>/', DepartmentViewSet.as_view({'get' : 'retrieve'}), name="department-retrieve"),
    path('<int:id>/update/', DepartmentViewSet.as_view({'put' : 'update'}), name="department-update"),
    path('<int:id>/delete/', DepartmentViewSet.as_view({'delete' : 'destroy'}), name="department-destroy"),
]