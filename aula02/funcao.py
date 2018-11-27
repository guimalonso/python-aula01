#!/usr/bin/python3

def ler_arquivo(nome):
    with open(nome, 'r') as arquivo:
        return arquivo.readlines()

def escrever_arquivo(nome, str):
    with open(nome, 'a') as arquivo:
        arquivo.write(str+'\n')

def contar_linhas(nome):
    return ler_arquivo(nome).__len__()

print(ler_arquivo('teste.txt'))
escrever_arquivo('teste.txt', 'teste')
print(contar_linhas('teste.txt'))
