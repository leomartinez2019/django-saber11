from django.shortcuts import render, get_object_or_404

from clasification.models import School

def index(request):
    datos = School.objects.all()[:100]
    return render(request, 'clasification/clasificacion.html', {'datos': datos})

def detalle(request, dato_pk):
    skool = get_object_or_404(School, pk=dato_pk)
    return render(request, 'clasification/detalle.html', {'skool': skool})
