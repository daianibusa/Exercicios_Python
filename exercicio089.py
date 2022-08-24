#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletimAluno = []
while True:
    nome = str(input('Nome do aluno: ')).upper().strip()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    boletimAluno.append([nome, [nota1, nota2], media])

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()

    if resposta == 'N':
        break
print('+='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for indice, aluno in enumerate(boletimAluno):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.2f}')

while True:
    print('='*40)
    opcao = int(input('Mostrar as notas de qual aluno? [999 para interromper] '))
    if opcao == 999:
        print('FIM!!!')
        break
    if opcao <= len(boletimAluno):
        print(f'As notas de {boletimAluno[opcao][0]} são {boletimAluno[opcao][1]}')

