from django.db import models

# User import
from accounts.models import Host
from city.models import City
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
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.title


def upload_location(instance, filename):
    PostModel = instance.__class__
    try:
        new_id = PostModel.objects.order_by("id").last().id + 1
    except AttributeError:  # no folder in database
        new_id = 1
    return "%s/%s" % (new_id, filename)


class PropartyImage(models.Model):
    proparty = models.ForeignKey(Proparty, on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to=upload_location, null=True,
                              blank=True, width_field="width_field", height_field="height_field")
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.caption
