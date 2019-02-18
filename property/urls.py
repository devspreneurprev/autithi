from django.urls import path
from django.contrib import admin

from .views import PropartyListAPIView

urlpatterns = [
    path("", PropartyListAPIView.as_view()),
]