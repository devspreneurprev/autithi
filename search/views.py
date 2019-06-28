from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.db.models import Q

import datetime

# Create your views here.
from property.models import Proparty

class PropartySearchApiView(APIView):
    permission_classes = [AllowAny]

    
    def get(self, request):
        method_dict = request.GET
        begin_date = method_dict.get("begin_date")
        end_date = method_dict.get("end_date")
        if end_date<begin_date:
            return JsonResponse({"error": "invalid date"})

        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        print(begin_date, end_date)

        propartys = Proparty.objects.filter(
            ~Q(bookings__request_accepted_by_host=True) |
            Q(bookings__begin_date__gt=end_date) | 
            Q(bookings__end_date__lt=begin_date)
        )
        data = []
        for proparty in propartys:
            data.append({
                "title": proparty.title,
                "cost_per_unit": proparty.cost_per_unit
            })
        return JsonResponse({"data": data})

