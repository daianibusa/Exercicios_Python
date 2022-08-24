#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input('Nome do aluno: ')).upper().strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'EM RECUPERAÇÃO'
else:
    aluno['situacao'] = 'REPROVADO'
print('='*50)
print(f'O nome do aluno é {aluno["nome"]}')
print(f'Sua média é {aluno["media"]}')
print(f'Sua situação é {aluno["situacao"]}')