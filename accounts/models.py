from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
import datetime

# User import
from city.models import City
from autithi.utils.upload_location import upload_image_path

EMAIL_REGEX = '^[a-z0-9.@]*$'


class UserManager(BaseUserManager, models.Manager):
    def get_by_username(self, username):
        qs = self.get_queryset().filter(username=username)
        if qs.count() == 1:
            return qs.first()
        return None

    def create_user(self, email, username, full_name, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
            full_name=full_name,
            date_of_birth=datetime.datetime(1996, 7, 27),
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    '''
    python manage.py shell
    from city.models import City
    c = City(name='unknown city', description='unknown city', views=0)
    c.save()
    '''
    full_name = models.CharField(max_length=255)
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
    username = models.CharField(max_length=255,)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=255,)
    zipcode = models.CharField(max_length=120, default="1000",)
    profile_image = models.ImageField(upload_to=upload_image_path, null=True,
                                      blank=True, width_field="width_field", height_field="height_field")
    description = models.TextField(max_length=255,)
    profession = models.CharField(max_length=255,)
    id_image1 = models.ImageField(upload_to=upload_image_path, null=True,
                                  blank=True, width_field="width_field", height_field="height_field")
    id_imege2 = models.ImageField(upload_to=upload_image_path, null=True,
                                  blank=True, width_field="width_field", height_field="height_field")
    id_type = models.IntegerField(
        blank=True, null=True)  # 1=NID, 2=PID, 3=DL_ID
    facebook = models.CharField(max_length=255,)
    twitter = models.CharField(max_length=255,)
    linkedin = models.CharField(max_length=255,)
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    is_verified = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    is_staff = models.BooleanField(default=False,)
    is_admin = models.BooleanField(default=False,)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Host(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    about = models.TextField()
    created_at = models.DateField(auto_now_add=True,)
    updated_at = models.DateField(auto_now=True,)

    def __str__(self):
        return self.user.username
