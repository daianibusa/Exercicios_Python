#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numero = cont = soma = 0 #Declaração de variáveis, onde todas começam com 0.
numero = int(input('Informe um número (999 para Parar): '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Informe um número (999 para Parar): '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
print('FIM!')