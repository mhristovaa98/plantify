from django.urls import reverse
from django.views.generic import CreateView, ListView

from cares.forms import CareLogAddForm
from cares.mixins import CareStatisticsMixin
from cares.models import CareLog
from plants.models import Plant


class CareLogAddView(CreateView):
        model = CareLog
        form_class = CareLogAddForm
        context_object_name = 'care_log'
        template_name = 'cares/care-log-create.html'

        def get_initial(self):
            initial = super().get_initial()
            plant = Plant.objects.get(pk=self.kwargs['plant_id'])
            initial['plant'] = plant
            return initial

        def form_valid(self, form):
            plant = Plant.objects.get(pk=self.kwargs['plant_id'])
            form.instance.plant = plant
            return super().form_valid(form)

        def get_success_url(self):
            return reverse('plants:detail', kwargs={'pk': self.object.plant.pk})

class CareLogListView(CareStatisticsMixin,ListView):
    model = CareLog
    template_name = 'cares/care-log-list.html'