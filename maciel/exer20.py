# Inicializando listas para armazenar números pares e ímpares
numeros_pares = []
numeros_impares = []

# Lendo 6 números inteiros e classificando-os como pares ou ímpares
for _ in range(6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Mostrando os números pares e ímpares e calculando a soma dos pares
print("Números pares digitados:", numeros_pares)
print("Soma dos números pares:", sum(numeros_pares))
print("Números ímpares digitados:", numeros_impares)
print("Quantidade de números ímpares:", len(numeros_impares))
