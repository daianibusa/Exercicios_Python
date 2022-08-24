#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
numeros = list()
def sorteia(lista):
    print('Sorteando 5 vaLores da lista: ', end=' ')
    for contador in range(0, 5,):
        numero = randint(1, 20)
        lista.append(numero)
        print(f'{numero}', end=' ')
        sleep(0.3)
    print('PRONTO!!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(numeros)
somaPar(numeros)
