#Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada.
numero = float(input('Informe um número: '))
print('O número informado foi {}, seu dobro é {}, seu triplo é {} e sua raíz quadrada é {:.2f}'.format(numero,(numero * 2), (numero * 3), pow(numero, (1/2))))
