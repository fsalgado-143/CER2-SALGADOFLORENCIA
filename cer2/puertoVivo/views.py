from django.shortcuts import render
from .models import LugarPatrimonial, Categoria

def home(request):
    return render(request,'puertoVivo/home.html')

def catalogo(request):

    lugares = LugarPatrimonial.objects.all()

    return render(request,'puertoVivo/catalogo.html', {
        'lugares': lugares
    })
    

def base(request):
    return render(request,'puertoVivo/base.html')

# Create your views here.
