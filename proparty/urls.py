from django.urls import path
from django.contrib import admin

from .views import PropartyListAPIView, PropartyDetailAPIView,PropertyCreateAPIView

urlpatterns = [
    path("", PropartyListAPIView.as_view()),
    path("create/", PropertyCreateAPIView.as_view()),
    path("<slug>/", PropartyDetailAPIView.as_view()),

]