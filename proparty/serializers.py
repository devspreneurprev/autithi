from rest_framework.serializers import ModelSerializer

from .models import Proparty, PropartyImage


class PropartyDetailSerializer(ModelSerializer):
    class Meta:
        model = Proparty
        fields = (
            'host',
            'city',
            'title',
            'description',
            'cost_per_unit',
            'place_type',
            'rental_type',
            'house_rules',
            'cancellation_policy',
            'amenities',
            'number_of_badrooms',
            'number_of_bathrooms',
            'accommodates',
            'times_viewed',
            'created_at',
            'updated_at',
            # 'proparty',
            # 'caption',
            # 'image',
            'created_at',
            'updated_at',
        )


class PropartyListSerializer(ModelSerializer):
    class Meta:
        model = Proparty
        fields = (
            'title',
            'slug',
            'city',
            'place_type',
        )
