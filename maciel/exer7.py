# Definindo a tupla de vendas
vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

# Calculando a média das vendas
media_vendas = sum(vendas) / len(vendas)

# Calculando a variância das vendas
variancia = sum((x - media_vendas) ** 2 for x in vendas) / len(vendas)

# Calculando o desvio padrão das vendas
desvio_padrao = variancia ** 0.5

# Encontrando o menor e o maior valor das vendas
menor_valor = min(vendas)
maior_valor = max(vendas)

# Imprimindo os resultados
print("Média das vendas:", media_vendas)
print("Variância das vendas:", variancia)
print("Desvio padrão das vendas:", desvio_padrao)
print("Menor valor das vendas:", menor_valor)
print("Maior valor das vendas:", maior_valor)
