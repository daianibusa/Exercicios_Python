#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athlético-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('CLASSIFICAÇÃO CAMPEONATO BRASILEIRO 2021')
for t in times:
    print(t)
print('='*200)

#Os 5 primeiros times
print('OS 5 PRIMEIROS COLOCADOS SÃO: ')
print(times[:5])
print('='*100)
#Os últimos 4 colocados
print('OS 4 REBAIXADOS SÃO: ')
print(times[-4:])
print('='*100)

#Times em ordem alfabética
print('ORDEM ALFABÉTICA')
print(sorted(times))
print('='*100)

#Em que posição está o time da Chapecoense
print(f'O TIME DA CHAPECONESE ESTÁ NA {times.index("Chapecoense")+1}ª POSIÇÃO')
print('='*100)
