#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('+='*20)
print('CALCULANDO PROGRESSÃO ARITMÉTICA')
print('+='*20)
primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Infome a razão da PA: '))
termo = primeiroTermo
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')