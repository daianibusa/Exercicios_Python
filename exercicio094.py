#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
pessoa = dict()
pessoasLista = list()
media = soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoa['sexo'] = str(input('Sexo [F/M]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas F ou M')
    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']

    pessoasLista.append(pessoa.copy())
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO! Por favor, responsa apenas S ou N')
    if resposta == 'N':
        break
print('=' * 50)
print(pessoasLista)
print('=' * 50)
print(f'A) Ao todo, temos {len(pessoasLista)} pessoas cadastradas.')
media = soma / len(pessoasLista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in pessoasLista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) As pessoas com idade acima da média são ', end='')
for p in pessoasLista:
    if p['idade'] > media:
        print(f'{p["nome"]} ', end='')
print()