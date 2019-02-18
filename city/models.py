from django.db import models

# Create your models here.


def upload_location(instance, filename):
    PostModel = instance.__class__
    try:
        new_id = PostModel.objects.order_by("id").last().id + 1
    except AttributeError:  # no folder in database
        new_id = 1
    return "%s/%s" % (new_id, filename)


class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_location, null=True,
                              blank=True, width_field="width_field", height_field="height_field")
    description = models.TextField()
    views = models.IntegerField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.name
