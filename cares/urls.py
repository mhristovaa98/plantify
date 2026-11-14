from django.urls import path, include

from cares.views import CareLogAddView, CareLogListView

app_name = 'cares'

urlpatterns = [
    path('<int:plant_id>/add/', CareLogAddView.as_view(), name='add'),
    path('list/', CareLogListView.as_view(), name='list'),

]