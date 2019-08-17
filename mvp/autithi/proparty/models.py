from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.utils.text import slugify
# User import
from accounts.models import User, Address
from autithi.utils.location import upload_location
# Create your models here.
from .utils import get_read_time


class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.name


class Proparty(models.Model):
    host = models.ForeignKey(User, related_name='propartys', on_delete=models.CASCADE,)
    city = models.ForeignKey(City, related_name='propartys', on_delete=models.CASCADE, null=True, blank=True)
    address = models.OneToOneField(Address, related_name='propartys', on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    cost_per_unit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    place_type = models.CharField(max_length=255, null=True, blank=True)
    rental_type = models.CharField(max_length=255, null=True, blank=True)
    house_rules = models.TextField(null=True, blank=True)
    cancellation_policy = models.TextField(null=True, blank=True)
    amenities = models.CharField(max_length=255, null=True, blank=True)
    number_of_badrooms = models.IntegerField(null=True, blank=True)
    number_of_bathrooms = models.IntegerField(null=True, blank=True)
    number_of_guest = models.IntegerField(null=True, blank=True)
    accommodates = models.CharField(max_length=255, null=True, blank=True)
    times_viewed = models.IntegerField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)


class PropartyImage(models.Model):
    proparty = models.ForeignKey(Proparty, related_name='propartyimage', on_delete=models.CASCADE)
    caption = models.TextField()
    image = models.ImageField(upload_to=upload_location,)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.caption


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Proparty.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = f"{slug}-{qs.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_proparty_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_proparty_receiver, sender=Proparty)
