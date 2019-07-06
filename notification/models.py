from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
from accounts.models import User
from proparty.models import Proparty


class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE, blank=True, null=True)
    proparty = models.ForeignKey(Proparty, related_name='notifications', on_delete=models.CASCADE, blank=True, null=True)

    checked = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    # def get_absolute_url(self):
    #     print("start calling")
    #     return reverse("proparty:proparty", kwargs={"slug": self.proparty.slug})
