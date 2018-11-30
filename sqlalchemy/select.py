from sqlalchemy import select
from core import user_table

slct = select([user_table]).where(user_table.c.nome.like('%Guilherme%'))

for registro in slct.execute():
    print(registro)