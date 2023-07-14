from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewViewSet


router = DefaultRouter(trailing_slash=False)

router.register(r'news', NewViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
