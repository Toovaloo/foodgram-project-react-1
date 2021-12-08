from django.contrib import admin

from .models import Ingredient, Measure


@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class MeasureAdmin(admin.ModelAdmin):
    pass
