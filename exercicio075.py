#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais número: ')),
           int(input('Digite o últimoo número: ')))
print(f'Você digitou os números: {numeros}')
print('='*30)
print(f'Você digitou o número 9 {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'O primeiro número 3 aparece na posição {numeros.index(3) + 1}')
else:
    print('Você não digitou o número 3')
print(f'Os números pares digitados foram ', end='')
for numero in numeros:
    if numero % 2 == 0:
        print(numero, end=' ')