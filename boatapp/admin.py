from django.contrib import admin

from boatapp.models import Owner, Boat, BoatHistory


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Администратор для модели Owner"""
    list_display = ('name',)

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    """Администратор для модели Boat"""
    list_display = ('name', 'year', 'owner',)
    list_filter = ('owner', 'year',)


@admin.register(BoatHistory)
class BoatHistoryAdmin(admin.ModelAdmin):
    """Администратор для модели Boat"""
    list_display = ('boat', 'start_year', 'stop_year', 'owner',)
    list_filter = ('owner', 'boat',)

