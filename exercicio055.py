#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
menorPeso = 0
maiorPeso = 0
for pessoas in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O mario peso lido foi de {}kg'.format(maiorPeso))
print('O menor peso lido foi de {}kg'.format(menorPeso))

