#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Informe um número inteiro: '))
conversao = int(input('Escolha a base de conversão: \n 1 = BINÁRIO \n 2 = OCTAL \n 3 = HEXADECIMAL \n'))
if conversao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('O número {} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou uma opção inválida.')