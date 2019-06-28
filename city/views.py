from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import (AllowAny)


from .models import City
from .serializers import CityListSerializer

from property.serializers import (
    PropartyListSerializer,
)
from property.models import Proparty


class CityListApiView(ListAPIView):
	queryset = City.objects.all()
	serializer_class = CityListSerializer
	permission_classes = [AllowAny]


class CityDetailsApiView(ListAPIView):
	serializer_class = PropartyListSerializer
	permission_classes = [AllowAny]
	def get_queryset(self,*args,**kwargs):
		pk=self.kwargs.get('pk')
		

		queryset = Proparty.objects.filter(city=pk)
		return queryset


