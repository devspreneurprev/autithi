from django.urls import path

from .views import BookingAPIViews


urlpatterns = [
    path('booking', BookingAPIViews.as_views() ),
]
