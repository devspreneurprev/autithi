from django.shortcuts import render, Http404

# Create your views here.
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
)
from rest_framework.generics import (
    CreateAPIView, UpdateAPIView, RetrieveAPIView, UpdateAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# User defined import
from .models import User


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    # queryset = User.objects.filter(username=request.username)
    permission_classes = [AllowAny]

    def get_object(self, *args, **kwargs):
        # request = self.request
        username = self.kwargs.get("username")
        instance = User.objects.get_by_username(username)
        if instance == None:
            raise Http404("Product doesn't exist and this is a bad request")
        return instance


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    lookup_field = 'username'
    # queryset = User.objects.filter(username=request.username)
    permission_classes = [AllowAny]

    def get_object(self, *args, **kwargs):
        # request = self.request
        username = self.kwargs.get("username")
        instance = User.objects.get_by_username(username)
        if instance == None:
            raise Http404("Product doesn't exist and this is a bad request")
        return instance


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        # print("in Login view -> ", data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
