#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Cachorro', 'Gato', 'Leao', 'Python', 'Programaçao', 'Aprender', 'Coracao')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} tem as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
