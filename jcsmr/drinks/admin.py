from django.contrib import admin
from .models import Drink


# Register your models here.
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'alcoholic_beverage']
    readonly_fields = ['uploaded_at']
    serch_fields = ['name']
    list_filter = ['name', 'uploaded_at']

