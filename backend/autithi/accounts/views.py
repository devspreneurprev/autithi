import jwt
import json
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (CreateAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status

# User defined import
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)
from .models import User, Address


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        print(request.user)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserProfileAPIView(APIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        get_data = self.request.GET
        user_id = kwargs.get('id')
        data = {}

        try:
            user = get_object_or_404(User, id=user_id, is_active=True)
        except Exception as error:
            return JsonResponse({"error": str(error)})
        try:
            address = get_object_or_404(Address, id=user.address.id)
            data['address'] = address.address
        except Exception as error:
            pass

        data['full_name'] = user.full_name
        data['is_email_verified'] = user.is_email_verified
        data['is_phone_number_verified'] = user.is_phone_number_verified
        data['description'] = user.description
        data['facebook'] = user.facebook
        data['twitter'] = user.twitter
        data['linkedin'] = user.linkedin
        data['is_verified'] = user.is_verified
        data['updated_at'] = user.updated_at
        data['full_name'] = user.full_name
        return JsonResponse(data)


class UserProfileUpdateAPIView(APIView):
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        data = {}
        data = self.request.GET

        token = data.get("token")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if not token:
            return JsonResponse({})
        decodedPayload = jwt.decode(token, None, None)
        email = decodedPayload.get("email")
        user_id = decodedPayload.get("user_id")
        username = decodedPayload.get("username")

        full_name = data.get("full_name")
        profile_image = data.get("profile_image")
        description = data.get("description")
        profession = data.get("profession")
        facebook = data.get("facebook")
        twitter = data.get("twitter")
        linkedin = data.get("linkedin")
        address = data.get("address")
        street = data.get("street")
        postal_code = data.get("postal_code")
        city = data.get("city")
        country = data.get("country")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        try:
            user_instance = get_object_or_404(User, id=user_id, is_active=True)
        except Exception as error:
            return JsonResponse({"error": str(error)})

        address_instance = user_instance.address
        coun = Address.objects.filter(id=address_instance.id).update(
            address=address,
            street=street,
            postal_code=postal_code,
            city=city,
            country=country,
            latitude=latitude,
            longitude=longitude
        )
        address_instance = Address.objects.get(id=address_instance.id)
        user_instance.full_name = full_name,
        # user_instance.profile_image = profile_image,
        user_instance.description = description,
        user_instance.profession = profession,
        user_instance.facebook = facebook,
        user_instance.twitter = twitter,
        user_instance.linkedin = linkedin
        user_instance.save()
        return JsonResponse({"valid": "valid"})
