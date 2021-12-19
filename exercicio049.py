#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um número para ver sua tabuada: '))
print('+='*20)
print('A tabuada de {} é: '.format(numero))
print('+='*20)
for c in range (1, 11):
    print('{} X {} = {}'.format(numero, c, numero * c))
