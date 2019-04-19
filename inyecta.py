#from miapp.models import Colegios # Colegios es legacy de 2015
import random
from saber.models import Colegio
from pymongo import MongoClient

# este script es para llenar la base de datos desde mlab (mongodb)

#mongouri = "mongodb://leonardo:password@ds031893.mongolab.com:31893/prueba1"
mongouri = "mongodb://leonardo:colombo.1528@ds031893.mlab.com:31893/prueba1"
cliente = MongoClient(mongouri)
db = cliente.prueba1
# coleccion de datos calendario A de 2016
col2016a = db.saber2016a
#col = db.pruebas2015

ditto = {'evaluados': 'evaluados',
         'departamento': 'departamento',
         'competencias': 'promcompetenciasciudadan',
         'ciencias': 'promcienciasnaturales',
         'sociales': 'promsocialesyciudadanas',
         'municipio': 'nombremunicipio',
         'nombre': 'nombreinstitucion',
         'matematicas': 'prommatematica',
         'ingles': 'promingles',
         'naturaleza': 'naturaleza',
         'calendario': 'calendario',
         'lectura': 'promlecturacritica',
         'jornada': 'jornada',
         'codigo': 'codinst',
         'periodo': 'periodo',
         'razonamiento': 'promrazonamientocuantita'}

def populate_db():
    """
    esta funcion solo se ejecuta una vez para poblar la base de datos
    """
    cliente = MongoClient(mongouri)
    db = cliente.get_default_database()
    col = db.saber2016b
    cursor = col.find()
    #dato = cursor.next()
    while True:
        dato = cursor.next()
        school = Colegio(nombre=dato[ditto['nombre']], municipio=dato[ditto['municipio']],
                     departamento=dato[ditto['departamento']], calendario=dato[ditto['calendario']],
                     naturaleza=dato[ditto['naturaleza']], evaluados=int(dato[ditto['evaluados']]),
                     matematicas=dato[ditto['matematicas']], sociales=dato[ditto['sociales']],
                     competencias=dato[ditto['competencias']],ingles=dato[ditto['ingles']],
                     ciencias=dato[ditto['ciencias']], razonamiento=dato[ditto['razonamiento']],
                     lectura=dato[ditto['lectura']], jornada=dato[ditto['jornada']], periodo=dato[ditto['periodo']],
                     codigo=dato[ditto['codigo']])
        school.save()

# De aqui elimine competencias y razonamiento ya que no aparecen en el 2016 calendario A
def populate_from_mongo2016():
    """
    Trae datos de mLab para llenar la base de datos de 2016
    """
    cursor = col2016a.find()
    while True:
        dato = cursor.next()
        colegio = Colegio(nombre=dato[ditto['nombre']], municipio=dato[ditto['municipio']],
                     departamento=dato[ditto['departamento']], calendario=dato[ditto['calendario']],
                     naturaleza=dato[ditto['naturaleza']], evaluados=int(dato[ditto['evaluados']]),
                     matematicas=dato[ditto['matematicas']], sociales=dato[ditto['sociales']],
                     ingles=dato[ditto['ingles']],
                     ciencias=dato[ditto['ciencias']], 
                     lectura=dato[ditto['lectura']], jornada=dato[ditto['jornada']], periodo=dato[ditto['periodo']],
                     codigo=dato[ditto['codigo']])
        colegio.save()
