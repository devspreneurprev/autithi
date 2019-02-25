from django.db import models

# User import
from property.models import Proparty
from accounts.models import User
# Create your models here.


class Trip(models.Model):
    proparty = models.ForeignKey(
        Proparty, on_delete=models.CASCADE, related_name="proparty",)
    guest = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name="user",)
    begin_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=15, decimal_places=2,)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.guest.username
