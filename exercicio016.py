#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
numero = float(input('Digite um número: '))
print('A porção inteira do número {} é {}.'.format(numero, trunc(numero)))
