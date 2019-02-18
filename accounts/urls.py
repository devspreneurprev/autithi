from django.urls import path
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]