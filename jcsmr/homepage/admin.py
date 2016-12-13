from django.contrib import admin
from .models import HomePageImage, HomePageSlider
# Register your models here.
@admin.register(HomePageImage)
class HomePageImageAdmin(admin.ModelAdmin):
    pass
@admin.register(HomePageSlider)
class HomePageSliderAdmin(admin.ModelAdmin):
    pass