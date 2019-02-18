from django.conf.urls import url
from django.contrib import admin

from .api_views import (
    UserCreateAPIView,
    UserLoginAPIView
)

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]