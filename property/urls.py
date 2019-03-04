from django.urls import path
from django.contrib import admin

from .views import (
    PropartyListAPIView, 
    PropartyDetailAPIView, 
    PropartyCreateAPIView,
    PropertyUpdateAPIView,
    PropertyDeleteAPIView
    )

urlpatterns = [
    path("", PropartyListAPIView.as_view()),
    path('create/', PropartyCreateAPIView.as_view(), name='create'),
    path('<pk>/delete/',PropertyDeleteAPIView.as_view()),
    path('<pk>/update/',PropertyUpdateAPIView.as_view()),
    path('<slug>/', PropartyDetailAPIView.as_view()),




]