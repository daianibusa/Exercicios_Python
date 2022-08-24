#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = []
dados = []
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break

print(f'A lista de pessoas cadastradas é: {pessoas}')
print(f'No total, foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorPeso}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}] ', end='')
print(f'\nO menor peso foi de {menorPeso}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}] ', end='')

