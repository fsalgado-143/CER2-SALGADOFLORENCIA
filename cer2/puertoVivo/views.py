from django.shortcuts import render

def home(request):
    return render(request,'puertoVivo/home.html')

def catalogo(request):
    return render(request,'puertoVivo/catalogo.html')

def base(request):
    return render(request,'puertoVivo/base.html')

# Create your views here.
