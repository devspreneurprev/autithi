<<<<<<< HEAD
from django.conf.urls import url
from django.urls import include, path


from .views import ReviewListApiView

=======
from django.urls import path
from django.contrib import admin

>>>>>>> 9d11ff4c22cddaa12f123e7190c95d519dee348d
urlpatterns = [
    path('reviewlist/', ReviewListApiView.as_view())
]