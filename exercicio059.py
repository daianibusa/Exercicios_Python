#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    Suas opções: 
    [ 1 ] somar 
    [ 2 ] multiplica 
    [ 3 ] maior 
    [ 4 ] novos números 
    [ 5 ] sair do programa''')
    opcao = int(input('Informe a opção desejada: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('\033[1;32mA soma entre {} + {} = {}\033[m'.format(valor1, valor2, soma))
    elif opcao == 2:
        multiplica = valor1 * valor2
        print('\033[1;33mA multiplicação entre {} X {} = {}\033[m'.format(valor1, valor2, multiplica))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('\033[1;34mO maior valor entre {} e {} é {}\033[m'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('FIM!! VOLTE SEMPRE!!')
    else:
        print('Opção inválida. Tente novamente.')
    print('=+'*20)

