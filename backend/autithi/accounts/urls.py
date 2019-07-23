from django.urls import path
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserRegisterAPIView,
    UserLoginAPIView,
    UserProfileAPIView,
    UserProfileUpdateAPIView
)

urlpatterns = [
    path('login/', obtain_jwt_token),
    # path('login/', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('profile/<id>/', UserProfileAPIView.as_view(), name='profile'),
    path('profile/update/<id>/', UserProfileUpdateAPIView.as_view(), name='profile_update'),
]
