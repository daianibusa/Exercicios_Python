#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, c
# adastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('=' * 30)
print('      JOGO DA MEGA SENA       ')
print('=' * 30)
quantidade = int(input('Quantos jogos você quer fazer?? '))
lista = []
jogos = []
totalJogos = 1
while totalJogos <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totalJogos += 1
print('=+' * 3, f'SORTEANDO {quantidade} JOGOS', '=+' * 3)
for indice, valor in enumerate(jogos):
    print(f'JOGO {indice + 1}: {valor}')
    sleep(1)
print('>='* 5, 'QUE VOCÊ FIQUE MILIONÁRIO!!!', '>=' * 5)
