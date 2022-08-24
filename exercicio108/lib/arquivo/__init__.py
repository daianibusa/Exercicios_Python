from exercicio108.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')# rt quer dizer abra o arquivo para leitura
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')# wt+ quer dizer crie um arquivo de texto
        a.close()
    except:
        print('Houve um erro ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível abrir o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')# at quer dizer append (crie) uma nova pessoa no arquivo
    except:
        print('Houve um erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} incluído com sucesso.')
            a.close()




