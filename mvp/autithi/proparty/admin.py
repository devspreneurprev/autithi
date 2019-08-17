from django.contrib import admin

# Register your models here.
from .models import Proparty, City, PropartyImage

admin.site.register(Proparty)
admin.site.register(PropartyImage)
admin.site.register(City)
