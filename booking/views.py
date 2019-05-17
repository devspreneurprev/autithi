from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response

from .models import Booking

class BookingAPIView(APIView):
    # serializer_class = PropartyListSerializer
    queryset = Proparty.objects.all()
    permission_classes = [AllowAny]


    def get(self):
        print("in booking get\n\n")
        print("request -> ", self.request.GET["id"])
        queryset = Booking.objects.all()
        return Response("Booking")

    def post(self, request):
        print("post")

