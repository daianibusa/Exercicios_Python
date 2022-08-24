#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)
def notas(*nota, situacao=False):
    """
        --> FUNÇÃO PARA VERIFICAR AS INFORMAÇÕES DE UM ALUNO
    :param nota: NOTAS QUE UM ALUNO OBTEVE, ACEITA VÁRIAS NOTAS
    :param situacao: CAMPO OPCIONAL - SE TRUE, INFORMA SE A SITUAÇÃO DO ALUNO É BOA, RAZOÁVEL OU RUIM, SE FALSE, NÃO APRESENTA A INFORMAÇÃO
    :return: RETORNA O TOTAL DE NOTAS, A MAIOR NOTA, A MENOR NOTA, A MÉDIA E A SITUAÇÃO (SE SOLICITADA)
    """
    resultado = dict()
    resultado['total'] = len(nota)
    resultado['maior'] = max(nota)
    resultado['menor'] = min(nota)
    resultado['media'] = sum(nota) / len(nota)

    if situacao:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'BOA'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'RAZOÁVEL'
        else:
            resultado['situacao'] = 'RUIM'

    return resultado


resposta = notas(4.5, 5.8, 4, 3.5, 6, situacao=True)
print(resposta)
help(notas)