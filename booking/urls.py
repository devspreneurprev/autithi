from django.urls import path
from .views import BookingRequestAPIView, BookingCancelingAPIView, BookingAcceptedAPIView

urlpatterns = [
    path('request/', BookingRequestAPIView.as_view()),
    path('request_cancel/', BookingCancelingAPIView.as_view()),
    path('request_accepted/', BookingAcceptedAPIView.as_view())
]
