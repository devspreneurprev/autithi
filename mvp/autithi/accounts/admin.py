from django.contrib import admin

# Register your models here.
from .models import User, Address

admin.site.register(User)
admin.site.register(Address)

