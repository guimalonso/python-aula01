#!/usr/bin/python3

nomeArquivo = input('Digite o nome do arquivo: ')

try:
    with open(nomeArquivo, 'r') as arquivo:
        conteudo = arquivo.readlines()

    for n in range(len(conteudo)):
        conteudo[n] = '{}- {}'.format(n+1, conteudo[n])
    
    with open(nomeArquivo, 'w') as arquivo:
        arquivo.writelines(conteudo)
except FileNotFoundError:
    print('Arquivo não existe')