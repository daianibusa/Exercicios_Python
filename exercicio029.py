#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Informe a velocidade do veículo em km/h: '))
valorMulta = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado, pois excedeu o limite de velocidade que é de 80 km/h')
    print('O valor da multa é de R$ {:.2f}'.format(valorMulta))
else:
    print('Parabéns, você está dentro da velocidade permitida!! ')
