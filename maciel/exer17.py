# Lendo um número inteiro entre 100 e 999
numero = int(input("Digite um número inteiro entre 100 e 999: "))

# Imprimindo cada algarismo que compõe o número
print("Algarismos que compõem o número:")
print(numero // 100)
print((numero // 10) % 10)
print(numero % 10)
