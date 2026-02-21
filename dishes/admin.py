from django.contrib import admin
from .models import Dish, Category

# Utilisation UNIQUEMENT du décorateur (plus propre pour un Master)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display   = ("name", "price", "category", "available")
    list_filter    = ("available", "category")
    search_fields  = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ["category"]

# ATTENTION : Vérifiez qu'il n'y a PAS de admin.site.register(Category) en bas du fichier.