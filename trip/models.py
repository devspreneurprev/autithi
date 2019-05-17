from django.db import models

# User import
from property.models import Proparty
from accounts.models import User
from booking.models import Booking
# Create your models here.


class Trip(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, blank=True, null=True)
    begin_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    confirmed = models.BooleanField(default=True,blank=True)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)


    def __str__(self):
        return str(self.booking)
