#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.
somaIdade = 0
media = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
mulheresMenosVinte = 0
for pessoas in range(1, 5):
    print('=========={}ª PESSOA=========='.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    somaIdade += idade
    if pessoas == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresMenosVinte += 1
media = somaIdade / 4
print('A média de idade do grupo é {} anos.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomeHomemMaisVelho, maiorIdadeHomem))
print('Há {} mulheres com menos de 20 anos.'.format(mulheresMenosVinte))

