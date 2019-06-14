from django.db import models

# User import
from accounts.models import Host
from city.models import City
from recommendation.models import Recommendation
from autithi.utils.location import upload_location
# Create your models here.


class Proparty(models.Model):
    host = models.ForeignKey(Host, related_name='propartys', on_delete=models.CASCADE,)
    city = models.ForeignKey(City, related_name='propartys', on_delete=models.CASCADE,)
    recommendation = models.ForeignKey(Recommendation, related_name='propartys', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255,)
    slug = models.SlugField()
    description = models.TextField(blank=True, )
    cost_per_unit = models.DecimalField(max_digits=15,blank=True, decimal_places=2,)
    place_type = models.CharField(max_length=255,blank=True, )
    rental_type = models.CharField(max_length=255,blank=True, )
    house_rules = models.TextField(blank=True, )
    cancellation_policy = models.TextField(blank=True, )
    amenities = models.CharField(max_length=255,blank=True, )
    number_of_badrooms = models.IntegerField(blank=True, )
    number_of_bathrooms = models.IntegerField(blank=True, )
    accommodates = models.CharField(max_length=255,blank=True, )
    times_viewed = models.IntegerField(blank=True, )
    is_booked = models.BooleanField(default=False, blank=True)
    booked_from_date = models.DateField(auto_now_add=True)
    booked_to_date = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class PropartyImage(models.Model):
    proparty = models.ForeignKey(Proparty, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True,
                              blank=True, )
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.caption
