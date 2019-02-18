from rest_framework.serializers import ModelSerializer

from .models import Review


class ReviewListSerializer(ModelSerializer):
    class Meta:

        model = Review
        fields = [
            'trip',
            'user_review',
            'user_score',
        ]
