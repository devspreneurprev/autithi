from django.urls import path
from .views import PropartyDetailView
urlpatterns = [
    path('<id>/', PropartyDetailView.as_view(), name='detail'),
]
