from django.db import models

# User import
from accounts.models import Host
from city.models import City
from autithi.utils.upload_location import upload_image_path
# Create your models here.


class Proparty(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE,)
    city = models.ForeignKey(City, on_delete=models.CASCADE,)
    title = models.CharField(max_length=255,)
    slug = models.SlugField()
    description = models.TextField()
    cost_per_unit = models.DecimalField(max_digits=15, decimal_places=2,)
    place_type = models.CharField(max_length=255,)
    rental_type = models.CharField(max_length=255,)
    house_rules = models.TextField()
    cancellation_policy = models.TextField()
    amenities = models.CharField(max_length=255,)
    number_of_badrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    accommodates = models.CharField(max_length=255,)
    times_viewed = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    booked_from_date = models.DateField(auto_now_add=True)
    booked_to_date = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.title


class PropartyImage(models.Model):
    proparty = models.ForeignKey(Proparty, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True,
                              blank=True, )
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.caption
