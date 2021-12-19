#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Informe o preço do produto: '))
novoPreco = preco - (preco * (5/100))
valorDesconto = preco - novoPreco
print('O preço atual do produto é R$ {:.2f}.'
      '\nSeu novo preço, com desconto de 5% é R$ {:.2f}.'
      '\nO valor do desconto foi de R$ {:.2f}.'.format(preco, novoPreco, valorDesconto))
