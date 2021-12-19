# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome.
nome = input('Informe seu nome completo: '.strip()) #Retira os espaços antes e no fianl da frase
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))
primeiroNome = nome.split()
print('Seu primeiro nome tem {} letas'.format(len(primeiroNome[0])))
