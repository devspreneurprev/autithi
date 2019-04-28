from rest_framework.serializers import ModelSerializer

# from .models import Recommendation
from property.models import Proparty

class RecommendationListSerializer(ModelSerializer):
    class Meta:
        model = Proparty
        fields = (
            'id',
            'city',
            'title',
            'description',
            'cost_per_unit',
            'place_type',
            'rental_type',
            'number_of_badrooms',
            'number_of_bathrooms',
        )
