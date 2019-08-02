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
    path('api/proparty/', include('proparty.urls')),
    path('api/trip/', include('trip.urls')),
    path('api/booking/', include('booking.urls')),
    path('api/search/', include('search.urls')),
    path('api/notification/', include('notification.urls')),
    
    # path('api/token/auth/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)