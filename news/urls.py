from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewViewSet


router = DefaultRouter()

router.register(r'new', NewViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
