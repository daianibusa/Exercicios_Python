# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep

cor = ('\033[m',         # 0 - sem cor
       '\033[1;40;41m',  # 1 - vermelha
       '\033[1;40;42m',  # 2 - verde
       '\033[1;40;43m',  # 3 - amarelo
       '\033[1;40;44m',  # 4 - azul
       '\033[1;40;45m',  # 5 - roxo
       '\033[7;40m',     # 6 - branca
       )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cor[6], end='')
    help(com)
    print(cor[0], end='')
    sleep(2)


def titulo(mensagem, cores=0):
    tamanho = len(mensagem) + 4
    print(cor[cores], end='')
    print('~' * len(mensagem))
    print(f'  {mensagem}')
    print('~' * len(mensagem))
    print(cor[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!!!', 1)
