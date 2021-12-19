#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = input('informe uma cidade: ').strip()#Elimina os espaços antes e no final da frase
print(cidade[:5].upper() == 'SANTO')
