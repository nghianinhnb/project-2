from django.urls import include, path
from rest_framework import routers
from .views import TuitionDebtViewSet

router = routers.DefaultRouter()
router.register(r'tuition-debt', TuitionDebtViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
