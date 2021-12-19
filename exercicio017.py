#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.
from math import hypot
catetoOposto = float(input('Digite o comprimento do cateto oposto: '))
catetoAdjacente = float(input('Digite o comprimento do cateto adjacente:  '))
hipotenusa = hypot(catetoOposto,catetoAdjacente)
print('Para um triângulo retângulo que tem o cateto oposto = {:.2f} e cateto adjacente = {:.2f},'
      ' a hipotenusa é = {:.2f}.'.format(catetoOposto,catetoAdjacente,hipotenusa))
