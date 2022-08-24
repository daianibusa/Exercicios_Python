#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* numero):# * serve para dizer que são vários parãmetros e que serão desempacotados
    contador = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in numero:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'\nO total de valores apresentados foram {contador} ')
    print(f'O maior valor foi {maior}')

maior(1, 5, 4, 8, 9, 10)
maior(2, 7, 5)
maior(2, 4)
maior(1)
maior()
