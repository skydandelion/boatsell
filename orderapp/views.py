from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse

from boatapp.models import Boat
from orderapp.models import Order
from orderapp.services import send_order_email


# Create your views here.
class OrderCreateView(CreateView):
    """Контроллер для создания заказа"""
    model = Order
    fields = ('boat', 'name', 'email', 'message',)

    def get_success_url(self):
        """Возвращает путь к странице создания заказа"""
        return reverse('boatapp:boat_view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        """Возвращает контекст данных"""
        context_data = super(OrderCreateView, self).get_context_data(**kwargs)
        context_data['boat'] = get_object_or_404(Boat, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        """Метод для обработки формы отправки письма"""
        obj = form.save()
        send_order_email(obj)
        return super().form_valid(form)

