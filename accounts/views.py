from django.contrib import auth
from django.http import HttpRequest
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions, viewsets, status

from .models import *
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class MeViewSet(viewsets.GenericViewSet):

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=(permissions.IsAuthenticated,))
    def me(self, request: HttpRequest):
        if request.method == 'GET':
            user = UserSerializer(request.user).data
            return Response({'user': user})
        else:
            serializer = self.get_serializer(instance=request.user, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'user': serializer.data})

    @action(detail=False, methods=['POST'], serializer_class=UserSerializer)
    def login(self, request: HttpRequest):
        if request.user.is_authenticated: return Response()

        user = auth.authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )

        if user is None: return Response(status=status.HTTP_401_UNAUTHORIZED)

        auth.login(request, user)
        return Response({'user': user})

    @action(detail=False, methods=['GET'], serializer_class=UserSerializer)
    def logout(self, request: HttpRequest):
        auth.logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
