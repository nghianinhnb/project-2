from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserDetailView

urlpatterns = [
    path('api/v1/register', UserRegistrationView.as_view(), name='user-registration'),
    path('api/v1/login', UserLoginView.as_view(), name='user-login'),
    path('api/v1/logout', UserLogoutView.as_view(), name='user-logout'),
    path('api/v1/users/<int:pk>', UserDetailView.as_view(), name='user-detail'),
]
