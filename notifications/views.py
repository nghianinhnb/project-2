from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

from shared.permissions import IsOwner

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        queryset = Notification.objects.filter(user=self.request.user).order_by('-is_seen', '-created_at')
        return queryset

    def get_permissions(self):
        if self.action == 'retrieve':
            # Only the owner can retrieve the notification
            return [permissions.IsAuthenticated(), IsOwner()]
        elif self.action in ['list', 'update']:
            # Only authenticated users can list and update their own notifications
            return [permissions.IsAuthenticated(), IsOwner()]
        else:
            return super().get_permissions()
