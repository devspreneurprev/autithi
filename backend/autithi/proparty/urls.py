from django.urls import path
from django.contrib import admin

from .views import (
    PropartyListAPIView,
    PropartyDetailAPIView,
    PropertyCreateAPIView,
    PropertyDeleteAPIView,
    PropertyUpdateAPIView,

    PropartyImageListAPIView
)

urlpatterns = [
    path("", PropartyListAPIView.as_view()),
    path("create/", PropertyCreateAPIView.as_view()),
    path("image/", PropartyImageListAPIView.as_view()),
    path("delete/<id>", PropertyDeleteAPIView.as_view()),
    path("update/<id>", PropertyUpdateAPIView.as_view()),
    path("<id>/", PropartyDetailAPIView.as_view()),
]
