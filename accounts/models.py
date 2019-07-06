from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
import datetime

# User import
from city.models import City
from autithi.utils.location import upload_location

EMAIL_REGEX = '^[a-z0-9.@]*$'



class Address(models.Model):
    address = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=120, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)




class UserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
            date_of_birth=datetime.datetime(1996, 7, 27),
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    city = models.ForeignKey(City, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
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
    username = models.CharField(max_length=255,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=255,null=True, blank=True)
    address = models.OneToOneField(Address, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    description = models.TextField(max_length=255,null=True, blank=True)
    profession = models.CharField(max_length=255,null=True, blank=True)
    id_image1 = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    id_imege2 = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    id_type = models.IntegerField(null=True, blank=True)  # 1=NID, 2=PID, 3=DL_ID
    facebook = models.CharField(max_length=255,null=True, blank=True)
    twitter = models.CharField(max_length=255,null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    is_verified = models.BooleanField(default=False,null=True, blank=True)
    is_active = models.BooleanField(default=True,null=True, blank=True)
    is_staff = models.BooleanField(default=False,null=True, blank=True)
    is_admin = models.BooleanField(default=False,null=True, blank=True)

    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


