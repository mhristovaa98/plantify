from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from cares.models import CareLog
from plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
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
    model = Plant
    template_name = 'plants/plant-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['care_log'] = CareLog.objects.filter(plant=self.object)
        return context


class PlantEditView(UpdateView):
    model = Plant
    form_class = PlantEditForm
    template_name = 'plants/plant-edit.html'

    def get_success_url(self):
        return reverse('plants:detail', kwargs={'pk': self.object.pk})


class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plants/plant-delete.html'
    success_url = reverse_lazy('plants:list')



