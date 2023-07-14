from django.urls import path, include
from rest_framework import routers
from .views import TransactionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
