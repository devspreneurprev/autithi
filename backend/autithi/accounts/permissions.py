from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user


class IsOwnerAndAuth(BasePermission):
    message = 'you have to login and must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        try:
            return obj == request.user
        except:
            return False

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        return False
