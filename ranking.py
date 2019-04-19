from miapp.models import Colegios
from appsaber.models import Schule

def make_rank():
    lista = Colegios.objects.order_by('-promedio').exclude(evaluados__lt=5)

    for indx in range(len(lista)):
        escuela = lista[indx]
        escuela.puesto = indx + 1
        escuela.save()

def rankmachen():
    lista = Schule.objects.order_by('-promedio').exclude(evaluados__lt=5)

    for indx in range(len(lista)):
        escuela = lista[indx]
        escuela.puesto = indx + 1
        escuela.save()

def rank_calend_a():
    # Para el annio 2016:
    #lista = Schule.objects.filter(calendario="A").order_by('-promedio').exclude(evaluados__lt=5)
    # Para el annio 2015:
    lista = Colegios.objects.filter(calendario="A").order_by('-promedio').exclude(evaluados__lt=5)

    for indx in range(len(lista)):
        escuela = lista[indx]
        escuela.rank_calend_a = indx + 1
        escuela.save()
