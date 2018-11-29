from psycopg2 import connect

try:
    con = connect("host=localhost user=python password=4linux dbname=fundamentals")
    cur = con.cursor()
    # cur.execute("select * from usuario")
    # print(cur.fetchall())
    cur.execute("insert into usuario (nome, email, cpf, nascimento) values ('{}','{}','{}','{}')".format(
        'teste', 'teste@teste.com', 'xxx-xxx-xxx-xx', '02/01/1980'
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

