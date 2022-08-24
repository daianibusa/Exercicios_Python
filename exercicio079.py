#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listaNumeros = list()
while True:
    numero = int(input('Digite um número: '))
    if numero not in listaNumeros:
        listaNumeros.append(numero)
        print('Valor adicionado com sucesso.')
    else:
        print('Este valor já existe na lista.')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? S/N ')).strip().upper()[0]
    if resposta == 'N':
        break
print('='*50)
listaNumeros.sort()
print(f'Você digitou os números {listaNumeros}')

