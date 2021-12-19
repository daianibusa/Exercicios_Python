#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoAtual = date.today().year
totalMaior = 0
totalMenor = 0
for pessoas in range(1,8):
    anoNascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    if anoAtual - anoNascimento >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
print('Há {} pessoas MAIORES de idade!'.format(totalMaior))
print('E há {} pessoas MENORES de idade!'.format(totalMenor))
