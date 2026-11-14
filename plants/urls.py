from django.urls import path, include

from plants.views import PlantListView, PlantCreateView, PlantDetailView, PlantEditView, PlantDeleteView

app_name = 'plants'


urlpatterns = [
    path('', PlantListView.as_view(), name = 'list'),
    path('create/', PlantCreateView.as_view(), name = 'create'),
    path('<int:pk>/', include([
        path('', PlantDetailView.as_view(), name = 'detail'),
        path('edit/', PlantEditView.as_view(), name = 'edit'),
        path('delete/', PlantDeleteView.as_view(), name = 'delete'),
    ])),
]