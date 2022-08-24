#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listaNumero = []
maior = 0
menor = 0
for numero in range(0, 5):
    listaNumero.append(int(input(f'Digite um número na posição {numero}: ')))
    if numero == 0:
        maior = menor = listaNumero[numero]
    else:
        if listaNumero[numero] > maior:
            maior = listaNumero[numero]
        if listaNumero[numero] < menor:
            menor = listaNumero[numero]
print('='*30)
print(f'Você digitou os números {listaNumero}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for indice, valor in enumerate(listaNumero):
    if valor == maior:
        print(f'{indice}...', end='')
print()
print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for indice, valor in enumerate(listaNumero):
    if valor == menor:
        print(f'{indice}...', end='')
    
