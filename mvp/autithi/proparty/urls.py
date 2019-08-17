from django.urls import path
from .views import PropartyDetailView, CityPropertyListView
urlpatterns = [
    path('<int:pk>/', PropartyDetailView.as_view(), name='detail'),
    path('city/<int:id>', CityPropertyListView.as_view(), name='city'),
]
