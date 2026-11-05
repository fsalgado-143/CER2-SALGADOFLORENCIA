from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST

from .models import LugarPatrimonial, Categoria
from .forms import LugarPatrimonialForm

def home(request):
    imagenes_carrusel = [ 
        {
            'imagen': 'https://i.pinimg.com/736x/f3/ca/51/f3ca519b500e44e2fd1fe6c9347cfed1.jpg',
            'titulo': 'Patrimonio de Chile',
            'descripcion': 'Descubre nuestra riqueza cultural.'
        },
        {
            'imagen': 'https://ejemplo.com/imagen2.jpg',
            'titulo': 'Nuestra historia',
            'descripcion': 'Conoce los lugares que nos representan.'
        },
        {
            'imagen': 'https://ejemplo.com/imagen3.jpg',
            'titulo': 'Cultura y tradición',
            'descripcion': 'Preservemos nuestro patrimonio.'
        }
        ]
    
    lugares_destacados = LugarPatrimonial.objects.all()[:4]

    return render(request, 'puertoVivo/home.html', {
        'lugares_destacados': lugares_destacados,
        'imagenes_carrusel': imagenes_carrusel
    })

def catalogo(request):

    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
        categoria_seleccionada = int(categoria_id)
    else:
        lugares = LugarPatrimonial.objects.all()
        categoria_seleccionada = None

    return render(request, 'puertoVivo/catalogo.html', {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
    })
    

def base(request):
    return render(request,'puertoVivo/base.html')

def descripcion(request, id):
    lugar = get_object_or_404(LugarPatrimonial, id=id)

    return render(request, 'puertoVivo/descripcion.html', {
        'lugar': lugar
    })

#panel principal
@login_required
def panel_admin(request):

    lugares = LugarPatrimonial.objects.all()

    return render(request, 'puertoVivo/panelAdmin.html', {
        'lugares': lugares
    })

#crear patrimonio
@login_required
@permission_required('patrimonio.add_lugarpatrimonial',
                     raise_exception=True)
def crear_lugar(request):

    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('panel_admin')

    else:
        form = LugarPatrimonialForm()

    return render(request, 'puertoVivo/formLugar.html', {
        'form': form,
        'titulo': 'Crear patrimonio',
        'boton': 'Guardar'
    })

#modificar patrimonio
@login_required
@permission_required('patrimonio.change_lugarpatrimonial',
                raise_exception=True)
def editar_lugar(request, id):

    lugar = get_object_or_404(LugarPatrimonial, id=id)

    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST, instance=lugar)

        if form.is_valid():
            form.save()
            return redirect('panel_admin')

    else:
        form = LugarPatrimonialForm(instance=lugar)

    return render(request, 'puertoVivo/formLugar.html', {
        'form': form,
        'titulo': 'Modificar patrimonio',
        'boton': 'Guardar cambios'
    })

#eliminar patrimonio
@login_required
@permission_required('patrimonio.delete_lugarpatrimonial',
                     raise_exception=True)
@require_POST
def eliminar_lugar(request, id):

    lugar = get_object_or_404(LugarPatrimonial, id=id)

    lugar.delete()

    return redirect('panel_admin')

# Create your views here.
