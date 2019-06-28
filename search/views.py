from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse

# Create your views here.
from property import models

class PropartySearchApiView(APIView):
    permission_classes = [AllowAny]

    
    def get(self, request):
        method_dict = request.GET
        begin_date = method_dict.get("begin_date")
        end_date = method_dict.get("end_date")
        
        return JsonResponse({"data": method_dict})

