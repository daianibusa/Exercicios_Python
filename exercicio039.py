#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anoNascimento = int(input('Informe o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento
print('Quem nasceu em {} tem {} anos em {}'.format(anoNascimento, idade, anoAtual))
if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(18 - idade))
else:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))