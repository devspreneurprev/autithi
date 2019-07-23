# buildin section
from django.urls import path

# user define section
from .views import RecommendationListAPIView

urlpatterns = [
    path("", RecommendationListAPIView.as_view(), name="recommendation"),
]
