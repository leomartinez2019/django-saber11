from clasification.models import School
from saber2016.models import Colegio16

def test1():
    conteo = 0
    ten = School.objects.all()[:100]
    for elem in ten:
        name = elem.nombre
        res = Colegio16.objects.filter(nombreinstitucion__icontains=name)
        cad = '\n'.join([kol.nombreinstitucion for kol in res])
        if len(cad) == 0:
            conteo += 1
            print(name)
    print(conteo)
