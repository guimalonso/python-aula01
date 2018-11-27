#!/usr/bin/python3

conteudo = 5*['novo\n']

try:
    with open('teste1.txt', 'x') as arquivo:
        arquivo.writelines(conteudo)
except FileExistsError:
    print('Arquivo já existe')