#Seja a tupla entrada = (1000, 2000, 5, 15000, 12, 1, 0.5, -2, 1000).
#Elabore um script Python que, usando a instrução for, determine a soma de todos os números de valor menor do que 100.

tupla = (1000, 2000, 5, 15000, 12, 1, 0.5, -2, 1000)
soma = 0
for i in tupla:
    if i < 100:
        soma += i
print('A soma é: ',soma)