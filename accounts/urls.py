from django.urls import path
from django.contrib import admin

from .views import (
    UserRegisterAPIView,
    UserLoginAPIView,
    UserUpdateAPIView,
    UserDetailAPIView,
)

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('update/<username>/', UserUpdateAPIView.as_view(), name='update'),
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
]