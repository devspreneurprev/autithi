from rest_framework.serializers import ModelSerializer

from .models import City

class CityListSerializer(ModelSerializer):
	class Meta:
		model = City
		fields =[
		'id',
		'name',
		'image',
		'description'



		]
					
