from rest_framework import viewsets, permissions
from .serializers import *
from django.http import JsonResponse
from django.db import transaction

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = CourseSerializer
    queryset = CourseOfStudy.objects.all()
    
    def create(self, request):
        try:
            with transaction.atomic():
                department = dict(request.data).pop('department')
                department = Department.objects.get(id=department)
                level = dict(request.data).pop('level')
                level, _ = AcademicLevel.objects.get_or_create(level=level)
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                course = serializer.save()
                alc = AcademicLevelCourse.objects.create(course=course, level=level, department=department)
        except Exception as e:
            return JsonResponse({'success':False, 'message':str(e)}, status=400)
        return JsonResponse({'success':True, 'message':serializer.data})

class AcademicLevelCourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    serializer_class = AcademicLevelCourseSerializer
    queryset = AcademicLevelCourse.objects.all()
    
    

