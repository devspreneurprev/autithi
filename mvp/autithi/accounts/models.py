from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
import datetime


# User import
from autithi.utils.location import upload_location

EMAIL_REGEX = '^[a-z0-9.@]*$'


class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    description = models.TextField()
    views = models.IntegerField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.name


class AddressQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(tag__title__icontains=query)
        )
        return self.filter(lookups).distinct()


class AddressManager(models.Manager):
    def get_queryset(self):
        return AddressQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

    def create_or(self, *args, **kwargs):
        id = kwargs.get("id")
        del kwargs["id"]
        if id:
            instance = self.get_queryset().update(**kwargs)
            return self.get_queryset().get(id=instance), False
        return self.get_queryset().create(**kwargs), True


class Address(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=120, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    active = models.BooleanField(default=True)

    objects = AddressManager()


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[
            RegexValidator(
                regex=EMAIL_REGEX,
                message='Email must be alphanumaric or contain any of following". @"',
                code="invalid_email"
            )
        ]
    )
    is_email_verified = models.BooleanField(default=False, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    is_phone_number_verified = models.BooleanField(default=False, null=True, blank=True)
    address = models.OneToOneField(Address, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profession = models.CharField(max_length=255, null=True, blank=True)
    id_image1 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    id_image2 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    id_type = models.IntegerField(null=True, blank=True)  # 1=NID, 2=PID, 3=DL_ID
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    is_verified = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


def pre_save_create_address(sender, instance, *args, **kwargs):
    if not instance.address:
        instance.address = Address.objects.create(address='None')


pre_save.connect(pre_save_create_address, sender=User)
