#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = input('Informe o nome do aluno: ')
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
print('As notas do aluno(a) {} são: {:.2f} e {:.2f}.\nSua média é de {:.2f}'.format(nome, nota1, nota2, media))
