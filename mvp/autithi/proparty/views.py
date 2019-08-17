from django.shortcuts import render
from django.views.generic import DetailView
from .models import Proparty
# Create your views here.


class PropartyDetailView(DetailView):
    lookup_field = id
    template_name = ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context