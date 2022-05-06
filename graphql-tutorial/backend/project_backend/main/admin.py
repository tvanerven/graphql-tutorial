from django.contrib import admin

from main.models import Ingredient, Category


admin.site.register(Category)
admin.site.register(Ingredient)

