# Lendo um vetor com 20 números inteiros
vetor = []
for _ in range(20):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

# Eliminando elementos repetidos do vetor
vetor_sem_repeticao = list(set(vetor))

# Exibindo o vetor sem elementos repetidos
print("Vetor sem elementos repetidos:", vetor_sem_repeticao)
