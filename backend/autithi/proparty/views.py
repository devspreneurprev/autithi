from django.shortcuts import render
from rest_framework.response import Response
import jwt
# Create your views here.
from .serializers import (
    PropartyListSerializer,
    PropartyDetailSerializer,

    PropartyImageSerializer,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# User defined import
from .models import Proparty, PropartyImage
from accounts.models import User
from booking.mixins import LoginRequiredMixin

class PropartyListAPIView(ListAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyListSerializer
    permission_classes = [IsAuthenticated]


class PropartyDetailAPIView(RetrieveAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class PropertyCreateAPIView(CreateAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    permission_classes = [AllowAny]


class PropertyDeleteAPIView(DestroyAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class PropertyUpdateAPIView(UpdateAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class PropartyImageListAPIView(ListAPIView):
    queryset = PropartyImage.objects.all()
    serializer_class = PropartyImageSerializer
    permission_classes = [AllowAny]