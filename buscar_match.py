import json
import pymongo
from saber2017.models import Colegio
from clasification.models import School

cliente = pymongo.MongoClient("mongodb://mongoso:soRok.40.forty@cluster0-shard-00-00-ej7ez.mongodb.net:27017,cluster0-shard-00-01-ej7ez.mongodb.net:27017,cluster0-shard-00-02-ej7ez.mongodb.net:27017/<DATABASE>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = cliente.test

def testmongo():
    'db of schools and their data'
    collection = db.colegios
    col = collection.find_one({"nombreestablecimiento": {"$regex": "MARYMOUNT"}})
    return collection

def testsaber(cad):
    cole = Colegio.objects.filter(nombreinstitucion__icontains=cad)
    return cole

# Hay 413 datos que estan en django pero no en mongo
# Django tiene un total de 11105 datos (clasificacion de colegios)
def test_both():
    'checks mongodb and postgres django'
    cols = testmongo()
    schools = School.objects.all()
    conteo = 0
    for elem in schools:
        codigo = elem.codigo_dane
        kol = cols.find_one({"codigoestablecimiento": codigo})
        if kol:
            codigo_mongo = kol['codigoestablecimiento']
            assert codigo_mongo == codigo
        else:
            print("No se encontró {}".format(codigo))
            conteo += 1
    print("All good")
    print("No se encontraron {} datos".format(conteo))
