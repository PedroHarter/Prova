import math

raio_maior = float(input('Digite o valor do raio maior da coroa: '))
raio_menor = float(input('Digite o valor do raio menor da coroa: '))

area_coroa = math.pi * (raio_maior**2 - raio_menor**2)

print('A área da coroa é: %.2f' %area_coroa)