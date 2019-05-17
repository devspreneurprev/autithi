from django.urls import path
from .views import BookingRequestAPIView

urlpatterns = [
    path('request/', BookingRequestAPIView.as_view()),
]