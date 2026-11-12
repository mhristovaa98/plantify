from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from plants.forms import PlantCreateForm
from plants.models import Plant


# Create your views here.

class PlantListView(ListView):
    model = Plant
    template_name = 'plants/plant-list.html'
    context_object_name = 'plants'


class PlantCreateView(CreateView):
    model = Plant
    template_name = 'plants/plant-create.html'
    form_class = PlantCreateForm
    success_url = reverse_lazy('plants:list')

class PlantDetailView(DetailView):
    ...

class PlantEditView(UpdateView):
    ...

class PlantDeleteView(DeleteView):
    ...