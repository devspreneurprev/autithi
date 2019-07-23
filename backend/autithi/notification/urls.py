from django.urls import path
from .views import NotificationAPIView

urlpatterns = [
    path('', NotificationAPIView.as_view())
]
