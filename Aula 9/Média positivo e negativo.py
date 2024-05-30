quantidade_valores = 4
soma = 0
qtd_positivos = 0
qtd_negativos = 0

for i in range (quantidade_valores):
    numero = float(input('Digite o {}º número: '.format (i+1)))
    soma += numero
    if numero > 0:
        qtd_positivos +=1
    elif numero < 0:
        qtd_negativos +=1
        
media = soma / quantidade_valores

percentual_positivos = (qtd_positivos / quantidade_valores) * 100
percentual_negativos = (qtd_negativos / quantidade_valores) * 100

print('A média dos números é: ', media)
print('Quantidade de valores positivos:', qtd_positivos)
print('Quantidade de valores negativos:', qtd_negativos)
print('Percentual de valores positivos: {:.2f}%'.format (percentual_positivos))
print('Percentual de valores negativos: {:.2f}%'.format (percentual_negativos))