from collections import defaultdict, Counter

from saber2017.models import Colegio

DEPTS = ['BOLIVAR', 'QUINDIO', 'CALDAS', 'CORDOBA', 'NARIÑO', 'BOGOTA',
         'ATLANTICO', 'RISARALDA', 'ANTIOQUIA', 'MAGDALENA', 'CAUCA',
         'CESAR', 'LA GUAJIRA', 'CUNDINAMARCA', 'VALLE', 'SANTANDER']

def prom_por_dept(departamento):
    'Encuentra el promedio y el score mayor por departamento'
    cols = Colegio.objects.filter(departamento=departamento).order_by('-puntajeglobal')
    total = cols.count()
    valores = [elem.puntajeglobal for elem in cols]
    suma = sum(valores)
    maximo = max(valores)
#    print("{}: {}, {}".format(departamento, cols[0], cols[0].nombremunicipio))
    print("<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n</tr>".format(departamento, cols[0], round(maximo), cols[0].nombremunicipio))
    prom = suma / total
#    print("Promedio:{}, valor maximo: {}".format(prom, maximo))

def depts_municipios():
    'crea un diccionario con clave departamento y lista de municipios'
    diccio = defaultdict(set)
    colegios = Colegio.objects.all()
    for elem in colegios:
        diccio[elem.departamento].add(elem.nombremunicipio)
    return diccio

