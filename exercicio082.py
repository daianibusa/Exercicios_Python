#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
listaPares = []
listaImpares = []
while True:
    lista.append(int(input('Digite um valor: ')))

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [SN] ')).strip().upper()
    if resposta == 'N':
        break
        
for valor in lista:
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)
listaPares.sort()
listaImpares.sort()
print(f'A lista completa é {lista}')
print(f'A lista de números PARES é {listaPares}')
print(f'A lista de números ÍMPARES é {listaImpares}')