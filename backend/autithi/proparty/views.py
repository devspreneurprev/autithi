from django.shortcuts import render
from rest_framework.response import Response
import jwt
# Create your views here.
from .serializers import (
    PropartyListSerializer,
    PropartyDetailSerializer
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# User defined import
from .models import Proparty
from accounts.models import User
from booking.mixins import LoginRequiredMixin

class PropartyListAPIView(LoginRequiredMixin, ListAPIView):
    def get_queryset(self):
        print(self.request.user)
        # token = self.request.GET.get("foo")
        # decodedPayload = jwt.decode(token,None,None)
        # print("get_queryset -> ", token , "\n", decodedPayload,"\n\n")
        queryset = Proparty.objects.all()
        return queryset

    serializer_class = PropartyListSerializer
    permission_classes = [IsAuthenticated]


class PropartyDetailAPIView(RetrieveAPIView):
    queryset = Proparty.objects.all()
    serializer_class = PropartyDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class PropertyCreateAPIView(APIView):
    serializer_class = PropartyListSerializer
    permission_classes = [IsAuthenticated]
