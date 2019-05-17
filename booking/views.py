from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response

from .models import Booking
from property.models import Proparty

class BookingRequestAPIView(APIView):
    # serializer_class = PropartyListSerializer
    # queryset = Proparty.objects.all()
    permission_classes = [AllowAny]


    def get(self):
        queryset = Booking.objects.all()
        proparty_id = self.request.GET.get("proparty_id")
        proparty_title = self.request.GET.get("proparty_title")
        user = self.request.user

        if user.IsAuthenticated:
            if property_id is not None and proparty_title is not None:
                proparty = Proparty.objects.filter(id=proparty_id, title=proparty_title)
                if proparty.count()==1:
                    host = proparty.host
                    if host.count()==1
                        booking_instance = Booking.objects.create(user=user, proparty=proparty, host=host)
                        # here notify the host
        else:
            # redirect to login page
            pass

        return Response("Booking")

    def post(self, request):
        print("post")

class BookingAcceptedAPIView(APIView):
    permission_classes = [AllowAny]

class BookingCancelingAPIView(APIView):
    permission_classes = [AllowAny]