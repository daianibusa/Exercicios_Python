#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS QUERO MAIS '))
preco = float(input('Informe o preço das compras: R$ '))
condicaoPagamento = int(input('Informe a condição de pagamento: \n'
      '1 - Á vista em dinheiro ou cheque. \n'
      '2 - Á vista no cartão. \n'
      '3 - Em até 2x no cartão. \n'
      '4 - 3z ou mais no cartão. \n'
      'Sua escolha: '))
if condicaoPagamento == 1:
     total = preco - (preco * 10 / 100)
elif condicaoPagamento == 2:
      total = preco - (preco * 5 / 100)
elif condicaoPagamento == 3:
      total = preco
      parcela = total / 2
      print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))
elif condicaoPagamento == 4:
      total = preco + (preco * 20 /100)
      qtdaParcelas = int(input('Em quantas parcelas? '))
      parcela = total / qtdaParcelas
      print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(qtdaParcelas, parcela))
else:
      total = preco
      print('\033[1;31mOpção de pagamento inválida. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))
