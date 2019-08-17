from django.urls import path
from django.contrib import admin

from .views import (
    PropartyListAPIView,
    PropartyDetailAPIView,
    PropertyCreateAPIView,
    PropertyDeleteAPIView,
    PropertyUpdateAPIView,

    PropartyImageListAPIView,
    UserPropartyListAPIView
)

urlpatterns = [
<<<<<<< HEAD
    path("", PropartyListAPIView.as_view()),
    path("create/", PropertyCreateAPIView.as_view()),
<<<<<<< HEAD
<<<<<<< HEAD:backend/autithi/proparty/urls.py
=======
    path("image/", PropartyImageListAPIView.as_view()),
    path("delete/<id>", PropertyDeleteAPIView.as_view()),
    path("update/<id>", PropertyUpdateAPIView.as_view()),
>>>>>>> nayan
    path("<id>/", PropartyDetailAPIView.as_view()),
=======
    path("", PropartyListAPIView.as_view(), name='proparty_list'),
    path("create/", PropertyCreateAPIView.as_view(), name='proparty_create'),
    path("user/<id>", UserPropartyListAPIView.as_view(), name='user_proparty'),
    path("image/<id>", PropartyImageListAPIView.as_view(), name='proparty_images'),
    path("delete/<id>", PropertyDeleteAPIView.as_view(), name='delete_proparty'),
    path("update/<id>", PropertyUpdateAPIView.as_view(), name='update_proparty'),
    path("<id>/", PropartyDetailAPIView.as_view(), name='proparty_detail'),
>>>>>>> master
]
=======
    path("<slug>/", PropartyDetailAPIView.as_view()),
]

"""
git merge with common
common change
"""
>>>>>>> 667f0534ffc9f51f89046742bde5ea0483c9a221:proparty/urls.py
