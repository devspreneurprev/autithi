from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import ReviewListSerializer
from .models import Review

class ReviewListApiView(ListAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewListSerializer
	permission_classes = [AllowAny]

# Create your views here.
