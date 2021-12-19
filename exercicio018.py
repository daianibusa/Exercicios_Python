#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import  math
angulo = float(input('Informe o valor do ângulo: '))
#Math.radians converte o valor do ângulo para radiano para conseguir calcular seno, cosseno e tangente
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do seno do ângulo é {:.2f}. '
      '\nO valor do cosseno do ângulo é {:.2f}.'
      '\nO valor da tangente do ângulo é {:.2f}'.format(seno, cosseno, tangente))
