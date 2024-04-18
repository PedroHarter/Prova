#Escreva um script em linguagem Python para ler um número de unidade de comprimento (um fracionário) e
#mostre a área do círculo deste raio. Assuma com valor do pi 3.14159 (uma apropriada declaração deve ser dada
#a esta constante). A saída deveria ter a seguinte forma:
#A área do círculo de raio ___ unidades e ___ unidades.
#Se você desejar melhorar este código, exiba a mensagem: Erro: valores negativos não são permitidos. Se o valor
#de estrada for negativo.

import math

PI = 3.14159

raio = float(input('Digite o raio do circulo (em unidades): '))

if raio <0:
    print('Erro: Valores negativos não são permitidos.')
else:
    area = PI * raio ** 2
    
    print(f'A área do círculo de raio {raio:.2f} unidades é {area:.2f} unidades.')