import jwt
import json
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status

# User defined import
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserDetailSerializer,
)
from .models import User, Address
from .permissions import IsOwnerOrReadOnly

class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'id'
    serializer_class = UserDetailSerializer


class UserProfileUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'id'
    serializer_class = UserDetailSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        print(request.user)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
