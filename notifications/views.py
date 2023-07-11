from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

from shared.permissions import *

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'destroy', 'update']:
            # Only the owner can read, delete, and update the notification
            return [permissions.IsAuthenticated(), IsOwner()]
        elif self.action == 'list':
            # Only authenticated users can list their own notifications
            return [permissions.IsAuthenticated()]
        else:
            return super().get_permissions()
