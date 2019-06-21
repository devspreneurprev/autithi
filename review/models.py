from django.db import models

from property.models import Proparty
from accounts.models import User
# Create your models here.


class Review(models.Model):
    reviewed_on = models.ForeignKey(User, related_name='reviewed_on', on_delete=models.CASCADE, blank=True, null=True)
    reviewed_by = models.ForeignKey(User, related_name='reviewed_by', on_delete=models.CASCADE, blank=True, null=True)
    proparty = models.ForeignKey(Proparty, related_name='reviews', on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.BooleanField(blank=True, null=True) # 1 is created by user 0 is created by host
    text = models.TextField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return str(self.proparty)

# class PropartyReview(models.Model):
#     user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
#     trip = models.ForeignKey(Trip, related_name='reviews', on_delete=models.CASCADE)
#     review = models.TextField()
#     score = models.IntegerField()
#     created_at = models.DateField(auto_now_add=True,)
#     updated_at = models.DateField(auto_now=True,)

#     def __str__(self):
#         return self.trip

class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    user   = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)
