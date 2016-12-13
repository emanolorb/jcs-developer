from django.contrib import admin
from .models import Food


# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['uploaded_at']
    serch_fields = ['name', 'takeout', 'lunch', 'dinner']
    list_filter = ['name', 'uploaded_at', 'takeout', 'lunch', 'dinner']

