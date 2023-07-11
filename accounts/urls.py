from rest_framework import routers
from django.urls import path, include

from . import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'', views.MeViewSet, basename='me')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
