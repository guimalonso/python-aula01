from faker import Faker
from psycopg2 import connect

fake = Faker('pt-BR')

try:
    con = connect("host=localhost user=python password=4linux dbname=fundamentals")
    cur = con.cursor()

    for x in range(0,100):
        cur.execute("insert into usuario (nome, email, cpf, nascimento) values ('{}','{}','{}','{}')".format(
            fake.name(), fake.email(), fake.cpf(), fake.date_of_birth().strftime('%d-%m-%Y')
        ))
    con.commit()
except Exception as e:
    con.rollback()
    print(e)
    exit()
finally:
    try:
        cur.close()
        con.close()
    except Exception:
        print('Cursor não definido!')