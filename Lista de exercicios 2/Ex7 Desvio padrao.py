#De acordo com a tupla Vendas apresentada abaixo. Desenvolva umscript em linguagem Python que calcule a média, a Variância, o DesvioPadrão, o menor valor e o maior Valor deste conjunto.
#Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)
#Media = Ʃi Vendasi
#n
#Variância = Ʃi (Vendasi – Média)²
#n
#Desvio Padrão = raiz da variancia

import math

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

media = sum(Vendas) / len(Vendas)

soma_diferencas_quadradas = sum((venda - media) ** 2 for venda in Vendas)
variancia = soma_diferencas_quadradas / len(Vendas)

desvio_padrao = math.sqrt(variancia)

menor_valor = min(Vendas)
maior_valor = max(Vendas)

print('Média:',media)
print('Variância:',variancia)
print('Desvio padrão:',desvio_padrao)
print('Menor valor:',menor_valor)
print('Maior valor:', maior_valor)