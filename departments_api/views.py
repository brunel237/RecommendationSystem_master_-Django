from rest_framework import viewsets, permissions
from .serializers import *

class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
