from rest_framework import viewsets, permissions
from .models import Transaction
from .serializers import TransactionSerializer

from shared.permissions import IsOwnerOrAdmin

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
