from django.urls import path
from .views import *

app_name = "courses_api"

urlpatterns = [
    path('', CourseViewSet.as_view({'get' : 'list'}), name="course-list"),
    path('details/', AcademicLevelCourseViewSet.as_view({'get' : 'list'}), name="course-list-details"),
    path('new/', CourseViewSet.as_view({'post' : 'create'}), name="course-create"),
    path('<int:id>/', CourseViewSet.as_view({'get' : 'retrieve'}), name="course-retrieve"),
    path('<int:id>/update/', CourseViewSet.as_view({'put' : 'update'}), name="course-update"),
    path('<int:id>/delete/', CourseViewSet.as_view({'delete' : 'destroy'}), name="course-destroy"),

]