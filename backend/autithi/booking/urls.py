from django.urls import path
from .views import BookingRequestAPIView, BookingCancelingAPIView, BookingAcceptedAPIView, BookingDateAPIView

urlpatterns = [
    path('request/', BookingRequestAPIView.as_view()),
    path('request_cancel/', BookingCancelingAPIView.as_view()),
    path('request_accepted/', BookingAcceptedAPIView.as_view()),
    path('booking_date/<id>', BookingDateAPIView.as_view(), name='booking_date_list '),
]
