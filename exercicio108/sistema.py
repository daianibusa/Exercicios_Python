from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pessoa', 'Incluir Pessoa', 'Sair do Sistema'])
    # LISTAS PESSOAS DO ARQUIVO
    if resposta == 1:
        lerArquivo(arq)

    # CRIAR NOVA PESSOA
    elif resposta == 2:
        cabecalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)#Função que inclui as pessoas no arquivo pessoa.txt

    elif resposta == 3:
        cabecalho('\033[1;32mSaindo do sistema!! Volte sempre!\033[m')
        break
    else:
        print('\033[1;31mDigite uma opção válida! \033[m')
    sleep(2)

