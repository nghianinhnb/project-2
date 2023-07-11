from rest_framework import viewsets, permissions
from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            # Only admin users can create and update subjects
            return [permissions.IsAdminUser()]
        elif self.action == 'list':
            # Any authenticated user can list subjects
            return [permissions.IsAuthenticated()]
        else:
            return super().get_permissions()
