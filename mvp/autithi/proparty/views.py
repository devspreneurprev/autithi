from django.shortcuts import render
from django.views.generic import DetailView

from .models import Proparty, PropartyImage

class PropartyDetailView(DetailView):
    model = Proparty
    lookup_field = 'id'
    template_name = 'proparty/detail_view.html'

    def get_queryset(self):
        instance = super().get_queryset()
        images = PropartyImage.objects.filter(proparty=instance[0].id)
        #  print(instance)
        # print(instance[0].id)
        instance["images"] = images
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(type(context.get('object')))
        return context
