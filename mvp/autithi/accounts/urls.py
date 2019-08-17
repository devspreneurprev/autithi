from django.urls import path
from .views import (
    login_view,
    registration_view,
    logout_view,
    HomePageView,
    PropertyListView
)

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('registration/', registration_view, name="register"),
    path('', HomePageView.as_view(),name='city_list'),
    path('city/<int:id>', PropertyListView.as_view(),name='city'),
]
