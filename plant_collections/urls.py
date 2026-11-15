from django.urls import path, include

from plant_collections.views import CollectionAddView, CollectionDeleteView, \
    CollectionListView, CollectionDetailView, CollectionAddPlantsView

app_name = 'collections'

urlpatterns = [
    path('', CollectionAddView.as_view(), name='create'),
    path('list/', CollectionListView.as_view(), name = 'list'),
    path('<int:pk>/', include([
        path('detail/', CollectionDetailView.as_view(), name='detail'),
        path('add/', CollectionAddPlantsView.as_view(), name='add'),
        path('delete/', CollectionDeleteView.as_view(), name='delete'),
    ]))

]