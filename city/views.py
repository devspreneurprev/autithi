from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import (AllowAny)


from .models import City
from .serializers import CityListSerializer


class CityListApiView(ListAPIView):
	queryset = City.objects.all()
	serializer_class = CityListSerializer
	permission_classes = [AllowAny]

