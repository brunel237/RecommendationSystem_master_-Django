from rest_framework import viewsets, permissions
from .serializers import *

class FacultyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()
    
    