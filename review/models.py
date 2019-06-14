from django.db import models

from property.models import Proparty
from accounts.models import User
# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    trip = models.ForeignKey(Proparty, related_name='reviews', on_delete=models.CASCADE)
    user_review = models.TextField()
    user_score = models.IntegerField()
    property_review = models.TextField()
    proparty_score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.trip
