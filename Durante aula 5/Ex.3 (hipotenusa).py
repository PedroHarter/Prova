import math

cateto1 = float(input('Digite o comprimento do primeiro cateto: '))
cateto2 = float(input('Digite o comprimento do segundo cateto: '))

hipotenusa = math.sqrt((cateto1 ** 2 + cateto2 ** 2))

print('A hipotenusa do triângulo retângulo é: %.0f'%hipotenusa)