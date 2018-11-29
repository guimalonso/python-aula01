from pymongo import MongoClient
from bson import ObjectId

try:
    client = MongoClient()
    db = client['test']
except Exception as e:
    print(e)
    exit()

user = {"_id": 4, "nome": "novo"}
db.usuario.insert(user)
# busca = db.usuario.find()
# print(list(busca))