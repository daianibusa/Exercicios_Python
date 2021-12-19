#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('Vamos verificar se o número digitado é PAR ou ÍMPAR?? ')
print('==' * 40)
numero = int(input('Digite um número: '))
if (numero % 2) == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))
