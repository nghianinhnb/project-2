from django.urls import path, include
from rest_framework import routers
from .views import SubjectViewSet

router = routers.DefaultRouter()
router.register(r'subject', SubjectViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
