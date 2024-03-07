from django.contrib import admin

from apps.cakes.models import Cake


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title']
    search_fields = ['title']

