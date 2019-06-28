from django.contrib import admin

# Register your models here.
from .models import Proparty, PropartyImage

admin.site.register(Proparty)
admin.site.register(PropartyImage)