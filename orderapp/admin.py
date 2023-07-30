from django.contrib import admin

from orderapp.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для модели Order"""
    list_display = ('boat', 'email',)
    list_filter = ('boat',)