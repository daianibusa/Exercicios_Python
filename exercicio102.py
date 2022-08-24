#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(numero, show=False):
    """
        --> CALCULA O FATORIAL DE UM NÚMERO
    :param numero: INFOMRÇÃO PARA CALCULAR O FATORIAL
    :param show: SE TRUE, IRÁ MOSTRAR TODO O CÁCULO DO FATORIAL, SE FALSE, APRESENTA APENAS O RESULTADO
    :return: RETORNA O VALOR DO FATORIAL
    """
    fat = 1
    for contador in range(numero, 0, -1):
        if show:
            print(f'{contador}', end='')
            if contador > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        fat *= contador
    return fat

print(fatorial(6, show=True))
help(fatorial)


