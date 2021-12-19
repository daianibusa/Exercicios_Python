#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print('+='*20)
print(' TABUADA ')
print('+='*20)
while True:
    numero = int(input('Informe um número para ver sua tabuada: '))
    print('='*40)
    if numero < 0:
        break
    for i in range(1, 11):
        print(f'{numero} X {i} = {numero * i}')
    print('='*40)
print('FIM!!')