#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

#Ler os valores digitados para a matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = somaColuna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('=' * 30)

#Mostrar a matriz com os valores digitados
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}] ',end='')

        # A) A soma de todos os valores pares digitados.
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()

print('=' * 30)
print(f'A soma dos números pares é {somaPar}')

# B) A soma dos valores da terceira coluna.
for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaColuna}')

# C) O maior valor da segunda linha.
for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')