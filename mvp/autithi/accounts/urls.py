from django.urls import path
from .views import (
    login_view,
    registration_view,
    logout_view,
)

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('registration/', registration_view, name="register"),
    
]
