from django.urls import path
from .views import PropartyDetailView
urlpatterns = [
    path('<int:pk>/', PropartyDetailView.as_view(), name='detail'),
]
