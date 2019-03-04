from django.shortcuts import render

# Create your views here.
from .serializers import (
    PropartyListSerializer,
    PropartyDetailSerializer,
    PropartyCreateUpdateSerializer
)
from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView

    )
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    )
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# User defined import
from .models import Proparty
from .permissions import IsPropertyOwner


class PropartyListAPIView(ListAPIView):
    serializer_class = PropartyListSerializer
    queryset = Proparty.objects.all()
    permission_classes = [AllowAny]


class PropartyDetailAPIView(RetrieveAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

class PropartyCreateAPIView(CreateAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyCreateUpdateSerializer 
    permission_classes = [IsPropertyOwner]

class PropertyUpdateAPIView(UpdateAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyCreateUpdateSerializer
    permission_classes = []
    lookup_field = 'pk'


class PropertyDeleteAPIView(DestroyAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyCreateUpdateSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'