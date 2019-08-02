from django.db import models

# User import
from accounts.models import User, Address
from city.models import City
from recommendation.models import Recommendation
from autithi.utils.location import upload_location
# Create your models here.


class Proparty(models.Model):
    host = models.ForeignKey(User, related_name='propartys', on_delete=models.CASCADE,)
    city = models.ForeignKey(City, related_name='propartys', on_delete=models.CASCADE,)
    address = models.OneToOneField(Address, related_name='propartys', on_delete=models.CASCADE, null=True, blank=True)
    recommendation = models.ForeignKey(Recommendation, related_name='propartys', on_delete=models.CASCADE, null=True, blank=True)
    
    title = models.CharField(max_length=255,null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)

    cost_per_unit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    place_type = models.CharField(max_length=255,null=True, blank=True)
    rental_type = models.CharField(max_length=255,null=True, blank=True)
    house_rules = models.TextField(null=True, blank=True)
    cancellation_policy = models.TextField(null=True, blank=True)
    amenities = models.CharField(max_length=255,null=True, blank=True)
    number_of_badrooms = models.IntegerField(null=True, blank=True)
    number_of_bathrooms = models.IntegerField(null=True, blank=True)
    number_of_guest = models.IntegerField(null=True, blank=True)
    accommodates = models.CharField(max_length=255,null=True, blank=True)
    times_viewed = models.IntegerField(null=True, blank=True)
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)


class PropartyImage(models.Model):
    proparty = models.ForeignKey(Proparty, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True,
                              blank=True, )
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.caption
