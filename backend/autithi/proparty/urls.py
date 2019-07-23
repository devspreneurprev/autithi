from django.urls import path
from django.contrib import admin

from .views import PropartyListAPIView, PropartyDetailAPIView, PropertyCreateAPIView

urlpatterns = [
    path("", PropartyListAPIView.as_view()),
    path("create/", PropertyCreateAPIView.as_view()),
<<<<<<< HEAD:backend/autithi/proparty/urls.py
    path("<id>/", PropartyDetailAPIView.as_view()),

]
=======
    path("<slug>/", PropartyDetailAPIView.as_view()),
]

"""
git merge with common
common change
"""
>>>>>>> 667f0534ffc9f51f89046742bde5ea0483c9a221:proparty/urls.py
