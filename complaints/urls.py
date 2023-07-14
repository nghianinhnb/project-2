from django.urls import path, include
from rest_framework import routers
from .views import ComplaintViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'complaints', ComplaintViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
