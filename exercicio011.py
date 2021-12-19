#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
qtdeTinta = area / 2
print('A largura da parede é {}m e a altura é {}m, então sua área é {}m²'.format(largura, altura, area))
print('A quantidade de tinta necessária para pintá-la é {} litros'.format(qtdeTinta))
