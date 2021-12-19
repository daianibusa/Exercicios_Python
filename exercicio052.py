#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número: '))
total = 0
for i in range(1, numero +1):
    if numero % i == 0:
        print('\033[1;32m', end=' ')
        total += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(i), end=' \033[m')
print('\nO número {} foi divísivel {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

