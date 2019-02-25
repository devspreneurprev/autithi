from django.urls import path
from django.contrib import admin

from .views import (
    UserRegisterAPIView,
    UserLoginAPIView
)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
]