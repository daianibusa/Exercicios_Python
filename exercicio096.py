#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    totalArea = largura * comprimento
    print(f'A área de um terreno medindo {largura} X {comprimento} é {totalArea}m²')


print('CALCULANDO A ÁREA DE TERRONO')
print('=' * 30)
larg = float(input('LARGURA EM M²: '))
comp = float(input('COMPRIMENTO EM M²: '))
area(larg, comp)



