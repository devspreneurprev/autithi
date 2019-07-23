from django.urls import path


from .views import PropartySearchApiView


urlpatterns = [
    path('', PropartySearchApiView.as_view()),
]
