from rest_framework import serializers

from .models import User
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)


class UserDetailSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    id_image1 = serializers.SerializerMethodField()
    id_image2 = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "full_name",
            "email",
            # "is_email_verified",
            "username",
            "date_of_birth",
            "phone_number",
            # "is_phone_number_verified",
            # "address",
            "profile_image",
            "description",
            "profession",
            "id_image1",
            "id_image2",
            "id_type",
            "facebook",
            "twitter",
            "linkedin",
            # "is_verified",
            # "is_active",
            # "is_staff",
            # "is_admin",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "created_at",
            "updated_at",
        )

    def get_profile_image(self, profile_image):
        try:
            request = self.context.get('request')
            profile_image_url = profile_image.profile_image.url
            return request.build_absolute_uri(profile_image_url)
        except Exception as error:
            print(error)

    def get_id_image1(self, id_image1):
        try:
            request = self.context.get('request')
            id_image1_url = id_image1.id_image1.url
            return request.build_absolute_uri(id_image1_url)
        except Exception as error:
            print(error)

    def get_id_image2(self, id_image2):
        try:
            request = self.context.get('request')
            id_image2_url = id_image2.id_image2.url
            return request.build_absolute_uri(id_image2_url)
        except Exception as error:
            print(error)

# class UserProfileUpdateSerializer(Serializer):
#     class Meta:
#         model = User
#         fields = (
#             'email',
#             'full_name',
#         )


class UserCreateSerializer(serializers.ModelSerializer):
    password1 = CharField(label='Password')
    password2 = CharField(label='Confirm Password')

    class Meta:
        model = User
        fields = (
            'email',
            'full_name',
            'password1',
            'password2',
        )
        extra_kwargs = {
            "password1": {"write_only": True},
            "password2": {"write_only": True}
        }

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
        password = validated_data['password1']
        username = create_username(str(email))
        print(username)
        user_obj = User(
            email=email,
            username=username,
            full_name=full_name,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


def create_username(email):
    email = email.replace("@", "")
    return email


class UserLoginSerializer(serializers.ModelSerializer):
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
