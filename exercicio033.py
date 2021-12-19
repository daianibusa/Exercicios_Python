#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))
numero3 = int(input('Informe o terceiro número: '))
#Verificando o número menor
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
print('O menor valor digitado foi {}'.format(menor))

#Verificando o maior valor
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print('O maior valor digitado foi {}'.format(maior))
