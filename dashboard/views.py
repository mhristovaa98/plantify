
from django.views.generic import TemplateView

from cares.mixins import CareStatisticsMixin
from plant_collections.models import Collection
from plants.models import Plant


# Create your views here.

class HomeView(CareStatisticsMixin,TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_plants = Plant.objects.order_by('-date_added')[:4]
        total_plants = Plant.objects.count()
        collections = Collection.objects.all()

        context['collections'] = collections
        context['total_plants'] = total_plants
        context['plants'] = latest_plants

        return context

