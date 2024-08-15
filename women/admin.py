from django.contrib import admin
from .models import Women, Husband, Category


admin.site.register(Husband)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "is_published", 'cat')
    list_display_links = ("id", "title")
    ordering = ["time_create", "title"]
    list_editable = ('is_published',)
    list_per_page = 3


@admin.register(Category)
class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ['id', 'name']
