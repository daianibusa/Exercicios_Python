#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno é {:.2f}'.format(media))
if media >= 7.0:
    print('\033[1;32mAPROVADO')
elif media <= 6.9 and media >= 5:
    print('\033[1;34mEM RECUPERAÇÃO')
else:
    print('\033[1;31mREPROVADO')
