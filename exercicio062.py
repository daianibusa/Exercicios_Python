#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('+='*20)
print('CALCULANDO PROGRESSÃO ARITMÉTICA')
print('+='*20)
primeiroTermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Infome a razão da PA: '))
termo = primeiroTermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quntos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')
