from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Proparty, PropartyImage
from accounts.models import Address


class PropartyDetailView(DetailView):
    model = Proparty
    lookup_field = 'id'
    template_name = 'proparty/detail_view.html'

    def get_queryset(self):
        instance = super().get_queryset()
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image_list = PropartyImage.objects.filter(proparty=context['object'].id)
        context['image_list'] = image_list
        return context


# class CityPropertyListView(ListView):
#     model = Proparty
#     template_name = 'city_proparty_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         obj = Proparty.objects.filter(address__area__icontains='Sylate')
#         obj2 = Proparty.objects.filter(address__area__icontains='Dhaka')
#         context['obj'] = obj
#         context['obj2'] = obj2
#         print(obj)
#         return context


class CityPropertyListView(ListView):
    model = Proparty
    template_name = 'city_proparty_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        area_list = Address.objects.order_by().values_list('area').distinct()
        area_list = [each_area[0] for each_area in area_list]

        city_propartys = list()
        for each_area in area_list:
            if each_area:
                each = dict()
                each["area"] = each_area
                each["propartys"] = Proparty.objects.filter(address__area=each_area)
                city_propartys.append(each)
        context["city_propartys"] = city_propartys
        return context
