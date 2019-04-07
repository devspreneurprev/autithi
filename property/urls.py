from django.urls import path
from django.contrib import admin

from .views import PropartyListAPIView, PropartyDetailAPIView

urlpatterns = [
    path("", PropartyListAPIView.as_view()),
    path("<slug>/", PropartyDetailAPIView.as_view()),
]