from django.db import models
from accounts.models import User, Host
from property.models import Proparty
# user import


# Create your models here.
class Booking(models.Model):
    host = models.ForeignKey(Host, related_name='bookings', on_delete=models.CASCADE,)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE,)
    proparty = models.ForeignKey(Proparty, related_name='bookings', on_delete=models.CASCADE,)
    requested_by_user = models.BooleanField(default=True)
    request_accepted_by_host = models.BooleanField(default=False)
    begin_date = models.DateField(editable=True, blank=True, null=True)
    end_date = models.DateField(editable=True, blank=True, null=True)
    date_conflict = models.BooleanField(blank=True, null=True)
    booking_cancled = models.BooleanField(blank=True, null=True)
    requested_at = models.DateField(auto_now_add=True)
    request_accepted_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{} request to {}".format(str(self.user), str(self.host))
