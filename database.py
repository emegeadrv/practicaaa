from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://carlotarojano99:Harrybieber6795@cluster0.lwvc7cn.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db