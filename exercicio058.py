#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('\033[1;32m========== JOGO DA ADIVINHAÇÃ0 ==========')
print('\033[1;34mSOU UM COMPUTADOR E PENSEI EM UM NÚMERO ENTRE 0 A 10. SERÁ QUE VOCÊ CONSEGUE ADIVINHAR?\033[m')
numero = int(input('Qual é seu palpite? '))
numeroComputador = randint(0, 10)
cont = 1
while numero != numeroComputador:
    if numeroComputador > numero:
        numero = int(input('Mais.... Digite novamente: '))
    else:
        numero = int(input('Menos.... Digite novamente: '))
    cont += 1
print('\033[1;33mVocê acertou com {} tentativas. PARABÉNS!!!  \n''O número que eu pensei foi {}'.format(cont, numeroComputador))