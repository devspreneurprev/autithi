from django.conf.urls import url
from django.urls import include, path

from django.contrib import admin

from .views import CityListApiView

urlpatterns = [
    path('citylist/', CityListApiView.as_view())

]