#!/usr/bin/python3
nomeArquivo = input('Digite o nome do arquivo: ')
shebang = '#!/usr/bin/python3\n'

try:
    with open(nomeArquivo+'.py', 'x') as arquivo:
        arquivo.write(shebang)
except FileExistsError:
    try:
        with open(nomeArquivo+'.py', 'r') as arquivo:
            conteudo = arquivo.readlines()
            if conteudo[0] != shebang:
                conteudo.insert(0, shebang)
                with open(nomeArquivo+'.py', 'w') as arquivo:
                    arquivo.write(conteudo)
    except IndexError:
        with open(nomeArquivo+'.py', 'a') as arquivo:
            arquivo.write(shebang)    