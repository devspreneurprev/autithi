from django.db import models
from autithi.utils.location import upload_location
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_location, null=True,blank=True, width_field="width_field", height_field="height_field")
    description = models.TextField()
    views = models.IntegerField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.name
