from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return Response(UserSerializer(user).data)

class UserLogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            # Allow read and update for the owner
            self.permission_classes = [permissions.IsAuthenticated | IsOwner]
        return super(UserDetailView, self).get_permissions()

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read and update for the owner
        return request.user == obj
