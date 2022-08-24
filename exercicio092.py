#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#Obs. Considere que a pessoa se aposenta com 35 anos de contribuição
from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('Nome: ')).strip().upper()
anoNascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = datetime.now().year - anoNascimento
cadastro['carteiraTrabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['carteiraTrabalho'] != 0:
    cadastro['anoContratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário R$: '))
    cadastro['aposentadoria'] = (cadastro['anoContratacao'] - anoNascimento) + 35
print('=' * 30)
for chave, valor in cadastro.items():
    print(f'{chave} tem o valor de {valor}')

