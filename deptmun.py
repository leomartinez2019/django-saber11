from miapp.models import Colegios, Departamento, Municipio

def process():
    objetos = Colegios.objects.all().order_by('departamento')
    depts = []
    muns = []
    for elem in objetos:
        d = elem.departamento
        m = elem.municipio
        if d not in depts:
            muns = []
            dept = Departamento(nombre=d)
            dept.save()
            depts.append(d)
        if m not in muns:
            mun = Municipio(nombre=m, departamento=dept)
            mun.save()
            muns.append(m)
    return depts, muns
