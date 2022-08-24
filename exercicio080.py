#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
listaNumeros = []
for numeros in range(0, 5):
    numero = int(input(f'Digite o {numeros + 1}º valor: '))
    if numeros == 0 or numero > listaNumeros[len(listaNumeros) - 1]:
        listaNumeros.append(numero)
        print('Valor adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(listaNumeros):
            if numero <= listaNumeros[posicao]:
                listaNumeros.insert(posicao, numero)
                print(f'Valor adicionado na posição {posicao} da lista')
                break
            posicao += 1
print(f'Os valores digitados em ordem foram: {listaNumeros}')
