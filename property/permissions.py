from rest_framework import permissions


class IsPropertyOwner(permissions.BasePermission):

    def has_permission(self, request,abc):
        if request.user.is_verified:
            return True
        return False   

