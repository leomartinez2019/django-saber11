import random
import pymongo
from saber.models import Colegio

mongouri = "mongodb://mongoso:soRok.40.forty@cluster0-shard-00-00-ej7ez.mongodb.net:27017,cluster0-shard-00-01-ej7ez.mongodb.net:27017,cluster0-shard-00-02-ej7ez.mongodb.net:27017/<DATABASE>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
cliente = pymongo.MongoClient(mongouri)
db = cliente.test

excuidos = ['I.E.', 'ESCUELA', 'SEDE', '-', 'PRINCIPAL', 'INSTITUCION', '(', ')', 'COL', 'EDUCATIVA']

def test_db():
    colegios = Colegio.objects.filter(municipio="LETICIA")
    nombres = [colegio.nombre for colegio in colegios]
    return nombres

def test_mongo():
    col = db.colegios.find_one()
    print(col)
