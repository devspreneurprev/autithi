from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

from .models import User
from autithi.utils.make_unique_username import create_username


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'full_name',
            'date_of_birth',
            'phone_number',
            'zipcode',
            'created_at',
            'updated_at',
        )


class UserCreateSerializer(ModelSerializer):
    password1 = CharField(label='Password')
    password2 = CharField(label='Confirm Password')

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'date_of_birth',
            'password1',
            'password2',
        )
        extra_kwargs = {
            "password1": {"write_only": True},
            "password2": {"write_only": True}
        }

    # def validate(self, data):
    #     email = data['email']
    #     user_qs = User.objects.filter(email=email)
    #     if user_qs.exists():
    #         raise ValidationError("This user has already registered.")
    #     return data

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get("password2")
        password2 = value
        if password1 != password2:
            raise ValidationError("Passwords must match.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        full_name = validated_data['full_name']
        date_of_birth = validated_data['date_of_birth']
        password = validated_data['password1']
        username = create_username(str(email))
        print(username)
        user_obj = User(
            email=email,
            username=username,
            full_name=full_name,
            date_of_birth=date_of_birth,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserUpdateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'full_name',
        )

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.full_name = validated_data.get(
            'full_name', instance.full_name)
        instance.save()
        return instance


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate(self, data):
        return data
