#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for numeros in range (1, 501, 2):
    if numeros % 3 == 0:
      soma += numeros
      contador += 1
print('A soma de todos os {} valores solicitados é igual a {}'.format(contador, soma))

