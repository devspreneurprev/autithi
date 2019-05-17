from django.db import models
from accounts.models import User, Host
from property.models import Proparty
# user import


# Create your models here.
class Booking(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    proparty = models.ForeignKey(Proparty, on_delete=models.CASCADE,)
    requested_by_user = models.BooleanField(default=True)
    request_accepted_by_host = models.BooleanField(default=True)
    requested_at = models.DateField(auto_now_add=True)
    request_accepted_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
