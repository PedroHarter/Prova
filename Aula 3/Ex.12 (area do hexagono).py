import math

raio = float(input('Digite o raio do hexágono regular: '))

area_triangulo = (3 * math.sqrt(3) * raio**2) / 2
area_hexagono = 6 * area_triangulo

print('A área do hexágono regular é: %.2f' %area_hexagono)