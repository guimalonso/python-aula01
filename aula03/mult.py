class Pai:
    a = 'classe pai'

class Mae:
    a = 'classe mae'

class Filho(Pai, Mae):
    c = 'classe filho'

objeto = Filho()

print(objeto.a, objeto.c)