from rest_framework import viewsets, permissions
from .models import Transaction
from .serializers import TransactionSerializer

from shared.permissions import IsOwnerOrAdmin

class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        # Set the owner of the transaction to the currently authenticated user
        serializer.save(owner=self.request.user)
