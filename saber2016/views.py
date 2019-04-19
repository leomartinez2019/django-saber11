from django.shortcuts import render
from saber2016.models import Colegio16
from django.core import serializers
from saber2017.forms import ColegioForm

def home(request):
    datos = Colegio16.objects.filter(
                puntajeglobal__gt=72).order_by(
                '-puntajeglobal').exclude(evaluados__lt=5)[:100]
    encabezado = "Pruebas Saber 11 2016: Listado de los Mejores Colegios"
    contexto = {'datos': datos, 'encabezado': encabezado}
    return render(request, 'home16.html', contexto)

def detalle(request, slug, pk):
    valor = Colegio16.objects.get(pk=pk)
    colegio = valor
    valor = serializers.serialize("json", [valor])
    return render(request, 'detalle.html', {'datos': valor, 'colegio': colegio})

def proc_colegio(request):
    print("Comenzando")
    if request.method == 'POST':
        print("Segundo paso")
        form = ColegioForm(request.POST)
        print(form.as_p())
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            nombre_colegio = form.cleaned_data['colegio'].strip()
            print("Tercer paso")
            print(nombre_colegio)
            try:
                lista_colegios = Colegio16.objects.filter(nombreinstitucion__iregex=nombre_colegio)
                print(lista_colegios)
                if len(lista_colegios) == 0:
                    form = ColegioForm()
                    mensaje = "Intente de nuevo. No se encontraron datos"
                    return render(request, 'search_results.html', {'form': form, 'mensaje': mensaje})
                elif len(lista_colegios) >= 1:
                    return render(request, 'search_results.html', {'datos': lista_colegios, 'titulo': 'Resultados de la Búsqueda' })
            except Colegio16.DoesNotExist:
                form = ColegioForm()
                mensaje = "Intente de nuevo. No se encontraron datos"
                return render(request, 'search_results.html', {'form': form, 'mensaje': mensaje})
        else:
            form = ColegioForm()
            return render(request, 'search_results.html', {'form': form, 'data': 0})
    else:
        form = ColegioForm()
        return render(request, 'search_results.html', {'form': form, 'data': 0})
