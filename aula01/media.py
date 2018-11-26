#!/usr/bin/python3
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

if media >= 7:
    result = 'Aprovado'
elif media > 3:
    result = 'Recuperação'
else:
    result = 'Reprovado'

print('Resultado: {} Media: {}'.format(result, media))