from rest_framework import serializers
from .models import Booking

class BookingDateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "begin_date",
            "end_date",
        )