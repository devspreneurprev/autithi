from django.conf.urls import url
from django.urls import include, path

from django.urls import path

from django.contrib import admin

from .views import CityListApiView,CityDetailsApiView

urlpatterns = [
    path('', CityListApiView.as_view()),
    path('<pk>/', CityDetailsApiView.as_view()),
]