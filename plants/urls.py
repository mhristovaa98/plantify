from django.urls import path

from plants.views import PlantListView, PlantCreateView

app_name = 'plants'


urlpatterns = [
    path('', PlantListView.as_view(), name = 'list'),
    path('create/', PlantCreateView.as_view(), name = 'create'),
]