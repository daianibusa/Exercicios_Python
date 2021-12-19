#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[1;32;40mOs segmentos acima podem formar um triângulo!\033[m')
else:
    print('\033[1;31;40mOs segmentos acima não podem formar um triângulo!\033[m')
