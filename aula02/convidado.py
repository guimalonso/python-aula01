#!/usr/bin/python3

lista = []

while True:
    try:
        convidado = input('Informe o nome de um convidado ou "sair" para exibir a lista de convidados e sair do programa: ')
        if convidado.lower() == 'sair':
            raise ValueError
        else:
            lista.append(convidado)
    except ValueError:
        break

for nome in lista:
    print("""
        Convite
        Nome: {}
    """.format(nome))

