from django.shortcuts import render
# Create your views here.
from .serializers import (RecommendationListSerializer)
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)

# User defined import
from .models import Recommendation
from proparty.serializers import PropartyDetailSerializer


class RecommendationListAPIView(ListAPIView):

    def get_queryset(self):
        queryset = Recommendation.objects.all()
        print("RecommendationListAPIView first -> ", queryset.first())

        req = queryset.first()
        if req is not None:
            print("RecommendationListAPIView req -> ", req.propartys.all())
            return req.propartys.all()
        return queryset

    serializer_class = RecommendationListSerializer
    permission_classes = [AllowAny]
