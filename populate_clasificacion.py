import re
import math
#from clasification.models import School

from pandas_proc import get_data


def test1():
    'make sure we get the data'
    data = get_data()
    print(data[23])

def test2():
    'make sure we connect to db'
    cols = School.objects.all()
    print(cols)

def test3():
    'comprueba que todos los datos fueron ingresados'
    data_csv = get_data()
    datadb = School.objects.all()
    for elem in data_csv:
        cod = elem['codigo_dane']
        kol = School.objects.filter(codigo_dane=cod)
        if len(kol) == 0:
            print(cod)

# TODO: evitar o limpiar los nombres de colegios muy largos
#       antes de ingresar los datos
def proc():
    'populates db with data from csv file'
    data = get_data()
    conteo = 0
    for elem in data:
        #col = School(**elem)
        #col.save()
        conteo += 1
    print("Se ingresaron {} datos".format(conteo))

# Funciona:
def test4():
    'limpiar dato de nombre de colegio'
    # captura solo el nombre del colegio
    patron = "(.+) - No es"
    conteo = 0
    data = get_data()
    for elem in data:
        nombre = elem['nombre']
        if 'posible' in nombre:
            conteo += 1
            busca = re.search(patron, nombre)
            try:
                nuevo = busca.group(1)
                elem['nombre'] = nuevo
                for item in elem:
                    if isinstance(elem[item], float) and math.isnan(elem[item]):
                        elem[item] = None
            except AttributeError:
                continue
            print(elem)
            print(elem['matematicas'])
            if conteo > 3:
                break
    print(conteo)

test4()

