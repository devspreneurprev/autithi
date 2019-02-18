<<<<<<< HEAD
from django.conf.urls import url
from django.urls import include, path

=======
from django.urls import path
>>>>>>> 9d11ff4c22cddaa12f123e7190c95d519dee348d
from django.contrib import admin

from .views import CityListApiView

urlpatterns = [
    path('citylist/', CityListApiView.as_view())

]