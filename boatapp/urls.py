from django.urls import path

from boatapp.apps import BoatappConfig
from boatapp.views import BoatListView, BoatDetailView

app_name = BoatappConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),  # путь к списку лодок
    path('<int:pk>/', BoatDetailView.as_view(), name='boat_view'),  # путь к карточке лодки
]