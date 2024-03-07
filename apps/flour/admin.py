from django.contrib import admin

from apps.flour.models import Flour


@admin.register(Flour)
class FlourAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title']
    search_fields = ['title']


