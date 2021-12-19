#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o salário do colaborador: R$ '))
novoSalario = salario + (salario * (15/100))
valorAumento = novoSalario - salario
print('O salário atual do colaborador é R$ {:.2f}.'
      '\nSeu novo salário, com 15% de aumento, será de R$ {:.2f}.'
      '\nSeu aumento foi de R$ {:.2f}'.format(salario,novoSalario,valorAumento))
