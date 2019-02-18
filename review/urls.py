from django.conf.urls import url
from django.urls import include, path


from .views import ReviewListApiView


from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('reviewlist/', ReviewListApiView.as_view())
]