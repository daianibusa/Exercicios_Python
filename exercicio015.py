#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
qtdaKm = float(input('Informe a quantidade de KM rodados com o veículo: '))
qtdaDias = int(input('Informe a quantidade de dias que ficou com o carro: '))
valor = (qtdaKm * 0.15) + (qtdaDias * 60)
print('Para um carro que rodou {}KM em {} dias, o preço a pagar é de R$ {:.2f}'.format(qtdaKm,qtdaDias,valor))
