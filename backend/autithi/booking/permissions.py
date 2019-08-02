from rest_framework.permissions import IsAuthenticated, BasePermission
import json
import jwt
from django.http import JsonResponse
from accounts.models import User
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class IsOwnerAndAuth(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        try:
            return obj.user == request.user
        except:
            return False

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False
