#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
listaNumeros = [[], []]
numero = 0
for numeros in range(1, 8):
    numero = (int(input(f'Digite o {numeros}º número: ')))
    if numero % 2 == 0:
        listaNumeros[0].append(numero)
    else:
        listaNumeros[1].append(numero)
listaNumeros[0].sort()
listaNumeros[1].sort()
print(f'Os números PARES foram: {listaNumeros[0]}')
print(f'Os números ÍMPARES foram: {listaNumeros[1]}')
