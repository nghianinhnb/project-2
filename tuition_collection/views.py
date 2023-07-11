from rest_framework import viewsets, permissions
from .models import TuitionCollection
from .serializers import TuitionCollectionSerializer

class TuitionCollectionViewSet(viewsets.ModelViewSet):
    queryset = TuitionCollection.objects.all()
    serializer_class = TuitionCollectionSerializer
    permission_classes = [permissions.IsAdminUser]
