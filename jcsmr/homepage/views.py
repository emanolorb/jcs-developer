from django.shortcuts import render
from .models import HomePageImage, HomePageSlider, HomePageText
# Create your views here.
def index(request):
    data = HomePageImage.objects.all()
    data1 = HomePageSlider.objects.all()
    data2 = HomePageText.objects.all()

    # validamos el query y si no damos valores a las variables
    if data:
        # Sacamos el nombre de cada imagen de portada
        for obj in data:
            nombre = '%s' %(obj.main_icon.name)
            nombre1 = '%s' %(obj.paralax_image1.name)
            nombre2 = '%s' %(obj.paralax_image2.name)
    else:
        nombre = '%s' %('')
        nombre1 = '%s' %('')
        nombre2 = '%s' %('')
    # validamos el query y si no damos valores a las variables
    if data2:
        # Sacamos el texto que va a llevar la pagina
        for obj1 in data2:
            texto = '%s' %(obj1.title)
            texto1 = '%s' %(obj1.subtitle)
            texto2 = '%s' %(obj1.blank_panel_text)
            texto3 = '%s' %(obj1.blank_panel_text_2)
            color = '%s' %(obj1.color_title)
            color1 = '%s' %(obj1.color_small_tag)
    else:
        texto = '%s' %('Titulo')
        texto1 = '%s' %('este es un subtitulo')
        texto2 = '%s' %('Titulo')
        texto3 = '%s' %('este es un subtitulo')
        color = '%s' %('lighten-5')
        color1 = '%s' %('lighten-5')
    context = {
        'img1' : nombre,
        'img2' : nombre1,
        'img3' : nombre2,
        'mainTitle' : texto,
        'mainDescription' : texto1,
        'blanktextTitle1' : texto2,
        'blanktextDescription1' : texto3,
        'data' : data1,
        'colorMaintitle' : color,
        'colorMainSubtitle' : color1,
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