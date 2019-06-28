"""autithi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include('accounts.urls')),
    path('api/city/', include('city.urls')),
    path('api/review/', include('review.urls')),
    path('api/recommendation/', include('recommendation.urls')),
    path('api/city/', include('city.urls')),
    path('api/property/', include('property.urls')),
    path('api/trip/', include('trip.urls')),
    path('api/booking/', include('booking.urls')),
    path('api/search/', include('search.urls')),
    path('api/token/auth/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
