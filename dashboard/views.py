
from django.views.generic import TemplateView

from plants.models import Plant


# Create your views here.

class HomeView(TemplateView):
    model = Plant
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_plants = Plant.objects.order_by('-date_added')[:4]
        total_plants = Plant.objects.count()
        context['total_plants'] = total_plants
        context['plants'] = latest_plants
        return context

