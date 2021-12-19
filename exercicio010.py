#Crie um prograama que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quantos reais você possúi? R$ '))
dolar = real / 5.34
euro = real / 6.26
libra = real / 7.30
print('Com R$ {:.2f} você consegue comprar US$ {:.2f}.'.format(real, dolar))
print('Com R% {:.2f} você consegue comprar € {:.2f}'.format(real, euro))
print('Com R$ {:.2f} você consegue comprar £ {:.2f}'.format(real, libra))
