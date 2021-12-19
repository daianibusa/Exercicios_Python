#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e mílimetros
medida = float(input('Digite a medida em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print('A medida de {}m corresponde a {}cm e {}mm'.format(medida, centimetros, milimetros))