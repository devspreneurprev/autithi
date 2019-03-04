from rest_framework import permissions

from .models import Proparty

class IsPropertyOwner(permissions.BasePermission):

    def has_permission(self, request,abc):
        if request.user.is_verified:
            return True
        return False   

