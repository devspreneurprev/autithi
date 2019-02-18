from django.conf.urls import url
from django.urls import include, path


from .views import ReviewListApiView

urlpatterns = [
    path('reviewlist/', ReviewListApiView.as_view())

]