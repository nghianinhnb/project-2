from django.urls import path, include
from rest_framework import routers
from .views import TuitionCollectionViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tuition-collection', TuitionCollectionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
