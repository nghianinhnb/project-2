from django.urls import path, include
from rest_framework import routers
from .views import NotificationViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
