from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from plant_collections.forms import CollectionAddForm, CollectionAddPlantsForm
from plant_collections.models import Collection


# Create your views here.

class CollectionListView(ListView):
    model = Collection
    template_name = 'collections/plant-collection-list.html'

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collections/plant-collection-detail.html'

class CollectionAddView(CreateView):
    model = Collection
    template_name = 'collections/plant-collection-add.html'
    form_class = CollectionAddForm
    success_url = reverse_lazy('collections:list')

class CollectionAddPlantsView(UpdateView):
    model = Collection
    form_class = CollectionAddPlantsForm
    template_name = 'collections/plant-collection-add-plant.html'

    def get_success_url(self):
        return reverse_lazy('collections:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        plant = form.cleaned_data['plants']
        self.object.plants.add(*plant)
        return redirect(self.get_success_url())


class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collections/plant-collection-delete.html'
    success_url = reverse_lazy('collections:list')