#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
numero = int(input('Digite o número que você acha que o computador escolheu, de 0 a 5: '))
num = randint(0, 6)
if numero == num:
    print('Parabéns, você acertou!!!')
else:
    print('Que triste, você perdeu, pois o número que o computador pensou foi {}!!'.format(num))
