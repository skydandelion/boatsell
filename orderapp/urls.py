from django.urls import path

from orderapp.apps import OrderappConfig
from orderapp.views import OrderCreateView

app_name = OrderappConfig.name

urlpatterns = [
    path('create/<int:pk>/', OrderCreateView.as_view(), name='create'),
]