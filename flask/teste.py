from faker import Faker
from connect import mongo_connect

fake = Faker('pt-BR')

db = mongo_connect('test')

for x in range(1,100):
    data = {
        "_id": x,
        "nome": fake.name(),
        "email": fake.email(),
        "cpf": fake.cpf(),
        "nascimento": fake.date_of_birth().strftime('%d-%m-%Y')
    }
    db.usuario.insert(data)