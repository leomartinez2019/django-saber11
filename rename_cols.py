import re

from saber2016.models import Colegio16

patron_gimn = "^GIMNASIO|^GIMNACIO|^GIMN\.|^GIMN"
patron_col = "COLEGIO|COL\.|COL "
patron = "COLEGIO |COL\.?\s"

def rename_cols(listado, patron, comienza, nuevo):
    'params: lista patron comienza nombre_nuevo'
    cont = 0
    for elem in listado:
        nombre = elem.nombreinstitucion
        if not nombre.startswith(comienza):
            continue
        nuevo_nombre = re.sub(patron, nuevo, nombre)
        elem.nombreinstitucion = nuevo_nombre
        #elem.save()
        print(elem.nombreinstitucion)
        cont += 1
        if cont > 30:
            break
    print("Bazinga!")

def test():
    cols = Colegio16.objects.all()
    rename_cols(cols, patron_col, 'COL', 'COLEGIO ')
