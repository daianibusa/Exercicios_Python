#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Informe seu peso: (KG) '))
altura = float(input('Informe sua altura: (M) '))
imc = peso / (altura * altura)
print('Seu IMC é {:.2f} kg/m2'.format(imc))
if imc < 18.5:
    print('Vocè está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso. CUIDADO!')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade. FAÇA EXERCÍCIOS!')
else:
    print('Vocẽ está com Obesidade Mórbida. PROCURE AJUDA MÉDICA! ')
