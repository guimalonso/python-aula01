#!/usr/bin/python3

soma = 0
qtde = int(input('Informe a quantidade de notas: '))

for n in range(qtde):
    try:
        nota = float(input('Digite a nota {}: '.format(n+1)))
    except ValueError:
        print('Nota inválida!')
        exit()
    if nota > 10:
        print('Nota inválida!')
        qtde -= 1
        continue
    soma += nota

media = soma / qtde

if media >= 7:
    result = 'Aprovado'
elif media > 3:
    result = 'Recuperação'
else:
    result = 'Reprovado'

print('Resultado: {} Media: {}'.format(result, media))