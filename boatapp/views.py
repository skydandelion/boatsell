from django.shortcuts import render
from django.views.generic import ListView, DetailView

from boatapp.models import Boat


class BoatListView(ListView):
    """Контроллер списка лодок"""
    model = Boat

class BoatDetailView(DetailView):
    """Контроллер подробной информации о лодке"""
    model = Boat
