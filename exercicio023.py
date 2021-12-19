#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número de 0 a 9999: '))
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(numero // 1 % 10))
print('Dezena: {}'.format(numero // 10 % 10))
print('Centena: {}'.format(numero // 100 % 10))
print('Milhar: {}'.format(numero // 1000 % 10))


