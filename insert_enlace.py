from miapp.models import Colegios
from appsaber.models import Schule
#from django.test import Client

# from insert_enlace import proceso
# pk_descartadas = [16, 628, 788, 12624, 12625, 12626, 29, 13008, 123]
# estas pk provocan errores en la appsaber (colegios con el mismo nombre)
pk_descartadas = []

def proceso():
    """
    compara la base de datos 2015 calendario b con enlaces para 2016
    testea los nuevos enlaces
    """
    datos15 = Colegios.objects.filter(calendario='B')
    contenedor = []
    #cliente = Client()
    control = True
    #datos16 = Schule.objects.all()
    # iterar para incorporar nuevo valor
    for elem in datos15:
        slug = elem.slug
        codigo = elem.codigo
        pk = elem.pk
        if pk in pk_descartadas:
            continue
        # asumo que el codigo es unico...
        # question = get_object_or_404(Question, pk=question_id)
        #schule = Schule.objects.get(codigo=codigo)
        #schule = get_object_or_404(Schule, codigo=codigo)
        try:
            schule = Schule.objects.get(codigo=codigo)
        except Schule.DoesNotExist:
            #print "pk: " + str(pk) + " codigo: " + codigo
            pk_descartadas.append(pk)
            continue
            #raise Http404("Schule does not exist")
        pk2 = str(schule.pk)
        enlace = "/saber2016/" + slug + "/" + pk2 + "/detalle/"
	contenedor.append(enlace)
        #response = cliente.get(enlace)
        #if response.status_code != 200:
            #control = False
            #print "Dammit!"
            #print "pk: " + elem.pk
            #break
    #if control:
    #print pk_descartadas
    print "Bazinga!!!"
    return pk_descartadas, contenedor


def procesar():
    """
    agrega campo enlace 2016 en la base de datos 2015 calendario b
    """
    datos15 = Colegios.objects.filter(calendario='B')
    contenedor = []
    control = True
    #datos16 = Schule.objects.all()
    # iterar para incorporar nuevo valor
    for elem in datos15:
        slug = elem.slug
        codigo = elem.codigo
        pk = elem.pk
        if pk in pk_descartadas:
            continue
        try:
            schule = Schule.objects.get(codigo=codigo)
        except Schule.DoesNotExist:
            print "Problemas..."
            continue
            #raise Http404("Schule does not exist")
        pk = str(schule.pk)
        enlace = "/saber2016/" + slug + "/" + pk + "/detalle/"
        elem.enlace = enlace
        elem.save()
    print "Work done!!!"

