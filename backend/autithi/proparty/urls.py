from django.urls import path
from django.contrib import admin

from .views import (
    PropartyListAPIView,
    PropartyDetailAPIView,
    PropertyCreateAPIView,
    PropertyDeleteAPIView,
    PropertyUpdateAPIView,

    PropartyImageListAPIView,
    UserPropartyListAPIView
)

urlpatterns = [
    path("", PropartyListAPIView.as_view(), name='proparty_list'),
    path("create/", PropertyCreateAPIView.as_view(), name='proparty_create'),
    path("user/<id>", UserPropartyListAPIView.as_view(), name='user_proparty'),
    path("image/<id>", PropartyImageListAPIView.as_view(), name='proparty_images'),
    path("delete/<id>", PropertyDeleteAPIView.as_view(), name='delete_proparty'),
    path("update/<id>", PropertyUpdateAPIView.as_view(), name='update_proparty'),
    path("<id>/", PropartyDetailAPIView.as_view(), name='proparty_detail'),
]