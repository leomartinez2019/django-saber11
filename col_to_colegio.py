import re

from saber2016.models import Colegio16

def test1():
    'check data before renaming'
    data = Colegio16.objects.filter(nombreinstitucion__regex='^COL\.')
    patron = "COL\.\s*"
    conteo = 0
    for elem in data:
        nombre = elem.nombreinstitucion
        nuevo = re.sub(patron, 'COLEGIO ', nombre)
        elem.nombreinstitucion = nuevo
        print(elem)
        elem.save()
        conteo += 1
    print("Se corrigieron {} registros".format(conteo))
