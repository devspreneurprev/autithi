from django.contrib import admin
from .models import Booking
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    fields = (
        'host',
        'user',
        'proparty',
        'begin_date',
        'end_date',
        'requested_by_user',
        'request_accepted_by_host',
    )
admin.site.register(Booking, BookingAdmin)
