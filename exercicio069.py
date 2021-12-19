#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
qtdaIdadeMaior18 = 0
qtdaHomens = 0
qtdaMulheres = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Informe o sexo (F/M): ')).strip().upper()[0]
    if idade >= 18:
        qtdaIdadeMaior18 += 1
    if sexo == 'M':
        qtdaHomens += 1
    if sexo == 'F' and idade < 20:
        qtdaMulheres += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Há {qtdaIdadeMaior18} pessoas maiores de 18 anos.')
print(f'Existem {qtdaHomens} homens cadastrados.')
print(f'E há {qtdaMulheres} mulheres com menos de 20 anos.')
