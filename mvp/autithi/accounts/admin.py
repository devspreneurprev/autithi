from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import User, Address

admin.site.register(User)
admin.site.register(Address)
admin.site.unregister(Group)
