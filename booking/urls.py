from django.urls import path
from .views import BookingAPIView

urlpatterns = [
    path('', BookingAPIView.as_view()),
]