from django.contrib import admin

# Register your models here.
from .models import Proparty, City

admin.site.register(Proparty)
admin.site.register(City)
