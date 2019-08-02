import datetime
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Booking
from proparty.models import Proparty
from accounts.models import User
from trip.models import Trip
from notification.models import Notification

from .mixins import LoginRequiredMixin
from .permissions import IsOwnerAndAuth
<<<<<<< HEAD

=======
>>>>>>> nayan

class BookingRequestAPIView(APIView):
    # serializer_class = PropartyListSerializer
    # queryset = Proparty.objects.all()
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerAndAuth]

    def date_in_range(self, begin_date, end_date, date):
        return begin_date <= date <= end_date

    def varifie_booking_date(self, begin_date, end_date, bookings):
        if begin_date > end_date:
            return False
        for booking in bookings:
            now_begin_date = str(booking.begin_date)
            now_end_date = str(booking.end_date)
            if self.date_in_range(now_begin_date, now_end_date, begin_date):
                return False
            if self.date_in_range(now_begin_date, now_end_date, end_date):
                return False
            if begin_date < now_begin_date and now_end_date < end_date:
                return False
        return True

    # parameter = (proparty_id, begin_date, end_date, guest_user)
    def get(self, request):
        print("start BookingRequestAPIView")
        proparty_id = self.request.GET.get("proparty_id")

        guest_user = self.request.GET.get("user")
        print(guest_user)
        # proparty_title = self.request.GET.get("proparty_title")
        guest_user = User.objects.get(email="nayan32biswas@gmail.com")

        if guest_user is not None:
            print(guest_user)
            if guest_user.is_verified == True:
                if proparty_id is not None:
                    proparty = Proparty.objects.get(id=proparty_id)
                    bookings = Booking.objects.filter(proparty=proparty_id, request_accepted_by_host=True)
                    begin_date = self.request.GET.get("begin_date")
                    end_date = self.request.GET.get("end_date")
                    if self.varifie_booking_date(begin_date, end_date, bookings):
                        host = proparty.host

                        booking_instance = Booking.objects.create(
                            user=guest_user,
                            proparty=proparty,
                            host=host,
                            requested_by_user=True,
                            begin_date=begin_date,
                            end_date=end_date
                        )
                        notification_instance = Notification.objects.create(
                            user=host,
                            proparty=proparty,
                            checked=False,
                            url=f'http://127.0.0.1:8000/api/proparty/?slug={proparty.slug}',
                            text=f"booking requested by {str(guest_user)}"
                        )
                        # here notify the host
            else:
                Response("User is not varified")
        else:
            Response("User is not logedin")
        return Response("Booking completed. Please wait for confirmation")

    def post(self, request):
        print("post")


class BookingAcceptedAPIView(APIView):
    permission_classes = [AllowAny]

    def varifie_booking_date(self, begin_date, end_date, bookings):

        if begin_date > end_date:
            return False
        for booking in bookings:
            now_begin_date = str(booking.begin_date)
            now_end_date = str(booking.end_date)
            if self.date_in_range(now_begin_date, now_end_date, begin_date):
                return False
            if self.date_in_range(now_begin_date, now_end_date, end_date):
                return False
            if begin_date < now_begin_date and now_end_date < end_date:
                return False
        return True

    # parameter = (booking_id, )
    def get(self, request):
        booking_id = request.GET.get("booking_id")

        try:
            print("start")
            booking_instance = Booking.objects.get(id=booking_id)
            print(booking_instance)
            begin_date = booking_instance.begin_date
            end_date = booking_instance.begin_date
            print("proparty")
            proparty_id = booking_instance.proparty

            bookings = Booking.objects.filter(proparty=proparty_id, request_accepted_by_host=True)
            print(proparty_id)
            if self.varifie_booking_date(begin_date, end_date, bookings):
                booking_instance.requested_by_user = False
                booking_instance.request_accepted_by_host = True
                booking_instance.save()
                trip_instance, trip_created = Trip.objects.get_or_create(
                    begin_date=booking_instance.begin_date,
                    end_date=booking_instance.end_date,
                    booking=booking_instance
                )
                if trip_created is not True:
                    return Response("alrady created")
                return Response("booking accepted")
        except:
            return Response("booking  error")


class BookingCancelingAPIView(APIView):
    permission_classes = [AllowAny]
    # parameter = (booking_id, )

    def get(self, request):
        booking_id = request.GET.get("booking_id")

        booking_instance = Booking.objects.get(id=booking_id)
        booking_instance.requested_by_user = False
        booking_instance.request_accepted_by_host = False

        trip_instance = Trip.objects.get(booking=booking_instance)
        trip_instance.confirmed = False

        booking_instance.save()
        trip_instance.save()

        print(trip_instance.confirmed)

        return Response(" Cancel confirm ")


class BookingDateAPIView(APIView):
    permission_classes = [AllowAny]

    # parameter = (proparty_id)
    def get(self, request):
        proparty_id = self.request.GET.get("proparty_id")
        booking_instance = Booking.objects.filter(proparty=proparty_id, request_accepted_by_host=True)
        booking_date_list = []
        print(booking_instance)
        for booking in booking_instance:
            booking_date_list.append((booking.begin_date, booking.end_date))
        print(booking_date_list)
        return JsonResponse({'booking_date_list': booking_date_list})
