# Inicializando a lista para armazenar os números
numeros = []

# Lendo 10 números reais
for _ in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

# Mostrando os números na ordem inversa
print("Números na ordem inversa:")
for numero in reversed(numeros):  # Utilizando a função reversed() para inverter a ordem dos elementos na lista
    print(numero)
