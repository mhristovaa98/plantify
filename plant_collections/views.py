from django.shortcuts import render
from django.views.generic import ListView

from plant_collections.models import Collection


# Create your views here.

class PlantCollectionListView(ListView):
    model = Collection
    template_name = 'collections/plant-collection-list.html'