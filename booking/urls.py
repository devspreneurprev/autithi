from django.urls import path
from .views import BookingRequestAPIView

urlpatterns = [
    path('request/', BookingAPIView.as_view()),
]