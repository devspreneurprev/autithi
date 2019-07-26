from rest_framework import serializers

from .models import Proparty, PropartyImage


class PropartyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proparty
        fields = '__all__'

class PropartyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proparty
        fields = (
            'id',
            'title',
            'slug',
            'city',
            'place_type',
        )


class PropartyImageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = PropartyImage
        fields = (
            'proparty',
            'caption',
            'photo_url',
            'created_at',
            'updated_at',
        )

    def get_photo_url(self, proparty_image):
        print("In PropartyImageSerializer")
        request = self.context.get('request')
        photo_url = proparty_image.image.url
        return request.build_absolute_uri(photo_url)
