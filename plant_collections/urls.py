from django.urls import path

from plant_collections.views import PlantCollectionListView

app_name = 'collections'

urlpatterns = [
    path('', PlantCollectionListView.as_view(), name = 'list'),
]