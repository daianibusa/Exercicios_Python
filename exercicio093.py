#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []
jogador['nome'] = str(input('Nome: ')).strip().upper()
totalPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for contador in range(0, totalPartidas):
    partidas.append(int(input(f'     Quantos gols {jogador["nome"]} fez na {contador+1}ª partida? ')))
jogador['gols'] = partidas[:]
jogador['totalGols'] = sum(partidas)
print('=' * 30)
print(jogador)
print('=' * 30)
for chave, vaor in jogador.items():
    print(f'{chave} tem o valor de {vaor}')
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {indice+1} foi um total de {valor}')
print(f'No total, forma {jogador["totalGols"]} gols marcados.')