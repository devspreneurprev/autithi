from django.db import models

# Create your models here.


class RecommendationManager(models.Manager):
    pass


class Recommendation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = RecommendationManager()

    def __str__(self):
        return self.name
