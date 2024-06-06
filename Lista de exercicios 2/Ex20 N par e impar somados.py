#– Faça um programa que receba 6 números inteiros e mostre:
#- Os números pares digitados
#- A soma dos números pares digitados
#- Os números ímpares digitados
#- A quantidade de números ímpares digitados

numeros_pares = []
numeros_impares = []

for i in range(6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print('Numeros pares digitados:', numeros_pares)
print('Soma dos numeros pares:', sum(numeros_pares))

print('Numeros impares digitados:',numeros_impares)
print('Quantidade de números impares:', len(numeros_impares))