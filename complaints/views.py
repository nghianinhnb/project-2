from rest_framework import viewsets, permissions
from .models import Complaint
from .serializers import ComplaintSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    def get_permissions(self):
        if self.action in ['create', 'list', 'retrieve']:
            # Only authenticated users can create and view their own complaints
            return [permissions.IsAuthenticated()]
        elif self.action == 'update':
            # Only staff members can update complaints
            return [permissions.IsAdminUser()]
        else:
            return super().get_permissions()
