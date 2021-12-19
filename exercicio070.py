#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('+='*30)
print('LISTA DE COMPRAS')
print('+='*30)
total = qtdaProdutosMaisMil = menorPreco = cont = 0
maisBarato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    print('='*30)
    cont += 1
    total += preco

    if preco > 1000:
        qtdaProdutosMaisMil += 1

    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        maisBarato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'O valor total da compra é R$ {total:.2f}')
print(f'Há {qtdaProdutosMaisMil} produtos que custam mais de R$ 1.000,00 cada.')
print(f'O produto com o menor preço é {maisBarato} e custa R$ {menorPreco:.2f}')