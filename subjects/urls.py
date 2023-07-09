from rest_framework import routers
from django.urls import path, include

# from . import views


router = routers.DefaultRouter()
# router.register('subject', views.UserViewSet, basename='user')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
