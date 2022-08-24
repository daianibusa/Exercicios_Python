#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
listaNumeros = []
while True:
    listaNumeros.append(int(input('Digite um valor: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('=' * 50)
print(f'Você digitou os números {listaNumeros}')
print(f'Há {len(listaNumeros)} números na lista.')
listaNumeros.sort(reverse=True)
print(f'A lista em ordem decrescente é {listaNumeros}')

if 5 in listaNumeros:
    print('O valor 5 está contido na lista.')
else:
    print('O valor 5 NÃO está na lista.')
