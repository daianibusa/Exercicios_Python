#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temperaturaGrausCelsius = float(input('Informe a temperatura em graus Celsius: '))
temperaturaGrausFahrenheit =((9 * temperaturaGrausCelsius) / 5) + 32
print('A temperatura de {:.1f}ºC, corresponde a  {:.1f}ºF.'.format(temperaturaGrausCelsius, temperaturaGrausFahrenheit))
