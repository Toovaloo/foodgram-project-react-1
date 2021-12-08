from django.contrib import admin

from .models import Ingredient, Measure


admin.site.register(Ingredient)
admin.site.register(Measure)
