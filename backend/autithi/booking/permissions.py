from rest_framework.permissions import IsAuthenticated, BasePermission
import json
import jwt
from django.http import JsonResponse
from accounts.models import User
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class IsOwnerAndAuth(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        try:
<<<<<<< HEAD
<<<<<<< HEAD
            print(self.request)
            return obj.user.user == self.request['user']
=======
            return obj.user.user == request.user
>>>>>>> nayan
=======
            return obj.user == request.user
>>>>>>> master
        except:
            return False

    def has_permission(self, request, view):
<<<<<<< HEAD
        print(request.GET)
        token_bearer = request.META.get('HTTP_AUTHORIZATION')
        token = token_bearer.split(" ")
        token = token[-1]
        data = {"token": token}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        if not token:
            return JsonResponse({})
        decodedPayload = jwt.decode(token, None, None)
        self.request = {}
        self.request['user'] = valid_data['user']
        email = decodedPayload.get("email")
        user_id = decodedPayload.get("user_id")

        user = User.objects.filter(username=self.request['user'])
        if user.exists():
            print("True")
            return True
        print("False")
=======
        if request.user and request.user.is_authenticated:
            return True
>>>>>>> nayan
        return False
