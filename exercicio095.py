#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: ')).strip().upper()
    totalPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for contador in range(0, totalPartidas):
        partidas.append(int(input(f'     Quantos gols {jogador["nome"]} fez na {contador+1}ª partida? ')))
    jogador['gols'] = partidas[:]
    jogador['totalGols'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO: Digite apenas S ou N;')
    if resposta == 'N':
        break
print('=' * 50)
#Cabeçalho
print('cod  ', end='')
for chave in jogador.keys():
    print(f'{chave:<15}', end='')
print()
#Dados da tabela
print('-' * 50)
for chave, valor in enumerate(time):
    print(f'{chave:>4} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 50)
#Mostrar levantamento de cada jogador
while True:
    busca = int(input('Quer mostrar os dsdos de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador de código {busca}!')
    else:
        print(f'    --LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for jogo, gol in enumerate(time[busca]["gols"]):
            print(f'    No jogo {jogo+1} fez {gol} gols')
    print('=' * 50)
print('>> VOLTE SEMPRE! >>')