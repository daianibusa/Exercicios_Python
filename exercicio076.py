#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Laranja', 1.98, 'Maçã', 3.99, 'Banana', 1.25, 'Tomate', 2.14,
           'Melancia', 1.39, 'Melão', 2.15, 'Uva', 5.58, 'Mamão', 2.29)
print('='*50)
print(f'{"MINHA FRUTARIA":^40}')
print('='*50)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<40}', end='')
    else:
        print(f'R$ {produtos[i]:>5.2f}')

