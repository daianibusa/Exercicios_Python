#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opção: 
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('-=' * 15)
print('Computador jogou \033[1;31m{}\33[m'.format(itens[computador]))
print('Jogador jogou \033[1;32m{}\033[m'.format(itens[jogador]))
print('-=' * 15)
if computador == 0:
    if jogador == 0:
        print('\033[1;33mEMPATOU\033[m')
    elif jogador == 1:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1.33mEMPATOU\033[m')
    elif jogador == 2:
        print('\033[1;32mJPGADOR VENCEU\033[m')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('\033[1;32mJOGADOR VENCEU\033[m')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCEU\033[m')
    elif jogador == 2:
        print('\033[1;33mEMPATOU\033[m')
    else:
        print('Jogada inválida!')
else:
    print('Jogada inválida!')
