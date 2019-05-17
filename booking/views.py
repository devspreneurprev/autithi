from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response

from .models import Booking
from property.models import Proparty
from accounts.models import User

class BookingRequestAPIView(APIView):
    # serializer_class = PropartyListSerializer
    # queryset = Proparty.objects.all()
    permission_classes = [AllowAny]


    def get(self, request):
        print("annonimous\n\n\n")
        queryset = Booking.objects.all()
        proparty_id = self.request.GET.get("proparty_id")
        # proparty_title = self.request.GET.get("proparty_title")
        print("\n\nid ->",proparty_id, "annonimous\n\n\n")
        user = User.objects.get(email="nayan32biswas@gmail.com")
        print("before condition ",user, "\n\n")
        if user is not None:
            print("after authentication",user)
            if proparty_id is not None:
                proparty = Proparty.objects.get(id=proparty_id)
                print(proparty.title,"\n\n")
                # if proparty.count()==1:
                print("proparty found\n\n")
                host = proparty.host
                print("host is -> ", host)
                # if host.count()==1:
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