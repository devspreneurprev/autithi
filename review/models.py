from django.db import models

from trip.models import Trip
# Create your models here.


class Review(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user_review = models.TextField()
    user_score = models.IntegerField()
    property_review = models.TextField()
    proparty_score = models.IntegerField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.trip
