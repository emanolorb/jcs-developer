from django.contrib import admin
from .models import HomePageImage, HomePageSlider, HomePageText
# Register your models here.
@admin.register(HomePageImage)
class HomePageImageAdmin(admin.ModelAdmin):
    pass
@admin.register(HomePageSlider)
class HomePageSliderAdmin(admin.ModelAdmin):
    pass
@admin.register(HomePageText)
class HomePageTextAdmin(admin.ModelAdmin):
    pass