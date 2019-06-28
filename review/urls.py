from django.conf.urls import url
from django.urls import include, path


from .views import (
    CreatePropartyReviewByUserApiView,
    CreateUserReviewByHostApiView,
    PropartyReviewListApiView,
    UserReviewListApiView,
    CreateCommentView
)


from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('create_property/', CreatePropartyReviewByUserApiView.as_view()),
    path('create_user/', CreateUserReviewByHostApiView.as_view()),
    path('create_comment/', CreateCommentView.as_view()),
    path('get_proparty/', PropartyReviewListApiView.as_view()),
    path('get_user/', UserReviewListApiView.as_view())
]
