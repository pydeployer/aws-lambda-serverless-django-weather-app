from django.contrib import admin

from weather.portal.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'lat', 'lon')
    search_fields = ('name', 'country')
    list_filter = ('country',)
    ordering = ('name',)
