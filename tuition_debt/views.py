from rest_framework import viewsets, permissions

from .models import TuitionDebt
from .serializers import TuitionDebtSerializer
from shared.permissions import IsOwner


class TuitionDebtViewSet(viewsets.ModelViewSet):
    queryset = TuitionDebt.objects.all()
    serializer_class = TuitionDebtSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow read-only access for the owner
            self.permission_classes = [permissions.IsAdminUser | IsOwner]
        else:
            # Allow CRUD operations for the admin
            self.permission_classes = [permissions.IsAdminUser]
        return super(TuitionDebtViewSet, self).get_permissions()
