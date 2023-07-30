from django.db import models

# Create your models here.
class Order(models.Model):
    """Модель заказа"""
    boat = models.ForeignKey('boatapp.Boat', on_delete=models.CASCADE, verbose_name='лодка')

    name = models.CharField(max_length=100, verbose_name='название заказа')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField(verbose_name='сообщение')

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.boat} от {self.email}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
