from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import (AllowAny, IsAuthenticated)

# Create your views here.
from accounts.models import User
from notification.models import Notification


class NotificationAPIView(APIView):
    permission_classes = [AllowAny]

    # parameter = (user)
    def get(self, request):
        user = self.request.GET.get("user")
        print(user)
        # proparty_title = self.request.GET.get("proparty_title")
        user = User.objects.get(email="nayan32biswas@gmail.com")
        print(user)
        notifications = Notification.objects.filter(user=user)
        print(notifications)
        data = []
        for each in notifications:
            temp = {}
            temp["user"] = str(each.user)
            temp["text"] = each.text
            temp["url"] = each.url
            data.append(temp)
        print("before end", data, "\n\n")
        return JsonResponse({"notification": data})

