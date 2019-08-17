from django.shortcuts import render
from django.views.generic import DetailView

from .models import Proparty, PropartyImage

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
