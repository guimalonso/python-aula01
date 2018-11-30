from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atlz = update(user_table).where(user_table.c.nome == 'Guilherme')

atlz = atlz.values(nome='Guilherme Alonso')

resultado = con.execute(atlz)

print(resultado.rowcount)