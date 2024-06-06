# Lendo um número inteiro positivo n
n = int(input("Digite um número inteiro positivo: "))

# Imprimindo o Triângulo de Floyd
numero_atual = 1
for linha in range(1, n + 1):
    for coluna in range(1, linha + 1):
        print(numero_atual, end=" ")
        numero_atual += 1
    print()
