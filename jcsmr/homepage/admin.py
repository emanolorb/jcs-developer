from django.contrib import admin
from .models import HomePageImage, HomePageSlider, HomePageText, ContactPageImage, HistoyPageImage
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
@admin.register(ContactPageImage)
class ContactPageImageAdmin(admin.ModelAdmin):
    pass
@admin.register(HistoyPageImage)
class HistoyPageImageAdmin(admin.ModelAdmin):
    pass
