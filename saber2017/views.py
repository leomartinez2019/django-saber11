from django.shortcuts import render
from saber2017.models import Colegio
from saber2016.models import Colegio16
from django.core import serializers
from .forms import ColegioForm

def home(request):
    datos = Colegio.objects.filter(
                puntajeglobal__gt=72).order_by(
                '-puntajeglobal').exclude(evaluados__lt=5)[:100]
    encabezado = "Pruebas Saber 11 2017: Listado de los Mejores Colegios"
    contexto = {'datos': datos, 'encabezado': encabezado}
    return render(request, 'home.html', contexto)

def detalle(request, slug, pk):
    valor = Colegio.objects.get(pk=pk)
    colegio = valor
    valor = serializers.serialize("json", [valor])
    return render(request, 'detalle.html', {'datos': valor, 'colegio': colegio})

def proc_colegio(request):
    #print("Comenzando")
    if request.method == 'POST':
        #print("Segundo paso")
        form = ColegioForm(request.POST)
        #print(form.as_p())
        #print(form.is_valid())
        #print(form.cleaned_data)
        if form.is_valid() and len(form.cleaned_data['colegio'].strip()) > 3:
            nombre_colegio = form.cleaned_data['colegio'].strip()
            #print("Tercer paso")
            #print(nombre_colegio)
            try:
                lista_colegios = Colegio.objects.filter(nombreinstitucion__iregex=nombre_colegio)
            except Colegio.DoesNotExist:
                lista_colegios = []
            try:
                lista_colegios16 = Colegio16.objects.filter(nombreinstitucion__iregex=nombre_colegio)
            except Colegio16.DoesNotExist:
                lista_colegios16 = []
            #print(lista_colegios)
            if len(lista_colegios) == 0 and len(lista_colegios16) == 0:
                form = ColegioForm()
                mensaje = "Intente de nuevo. No se encontraron datos"
                return render(request, 'search_results.html', {'form': form, 'mensaje': mensaje})
            elif len(lista_colegios) >= 1 or len(lista_colegios16) >= 1:
                lista_colegios = lista_colegios.union(lista_colegios16)
                return render(request, 'search_results.html', {'datos': lista_colegios, 'titulo': 'Resultados de la Búsqueda' })
        else:
            form = ColegioForm()
            return render(request, 'search_results.html', {'form': form, 'data': 0})
    else:
        form = ColegioForm()
        return render(request, 'search_results.html', {'form': form, 'data': 0})
