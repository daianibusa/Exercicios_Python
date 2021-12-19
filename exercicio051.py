#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('+='*20)
print('CALCULANDO PROGRESSÃO ARITMÉTICA')
print('+='*20)
primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Infome a razão da PA: '))
decimoTermo = primeiroTermo + (10 - 1) * razao
for i in range(primeiroTermo, decimoTermo + razao, razao):
    print('{} '.format(i), end='-> ')
print('FIM!')
