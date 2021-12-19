#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o valor do seu salário: R$ '))
anos = int(input('Infome em quantos anos deseja pagar o financiamento: '))
prestacao = (valorCasa / (anos * 12))
maximoComprometimento = salario * (30/100)
print('\033[1;33mPara pagar uma casa de R$ {:.2f} em {} anos, a prestação será de {:.2f}'.format(valorCasa, anos, prestacao))
if prestacao > maximoComprometimento:
    print('\033[1;31mEMPRÉSTIMO NEGADO!')
else:
    print('\033[1;32mEMPRÉSTIMO APROVADO!')
