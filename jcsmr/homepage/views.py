from django.shortcuts import render
from .models import HomePageImage, HomePageSlider
# Create your views here.
def index(request):
    data = HomePageImage.objects.all()
    data1 = HomePageSlider.objects.all()
    # get_aligned_caption_display    

    # Sacamos el nombre de cada imagen de portada
    for obj in data:
        nombre = '%s' %(obj.main_icon.name)
        nombre1 = '%s' %(obj.paralax_image1.name)
        nombre2 = '%s' %(obj.paralax_image2.name)
    context = {
        'img1' : nombre,
        'img2' : nombre1,
        'img3' : nombre2,
        'data' : data1,
    }
    return render(request, 'ini.html', context)

def contact(request):
    data = HomePageImage.objects.all()
    # Sacamos el nombre de cada imagen
    nombre = ''
    for obj in data:
        nombre = '%s' %(obj.main_icon.name)
        nombre1 = '%s' %(obj.paralax_image1.name)
        nombre2 = '%s' %(obj.paralax_image2.name)
    context = {
        'img1' : nombre,
        'img2' : nombre1,
        'img3' : nombre2,
    }
    return render(request, 'contact.html', context)