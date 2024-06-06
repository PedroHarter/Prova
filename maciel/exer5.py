# Lendo a lista de n valores inteiros
lista = []
n = int(input("Quantos valores você quer inserir na lista? "))
for i in range(n):
    valor = int(input(f"Digite o valor {i + 1}: "))
    lista.append(valor)

# Removendo os números ímpares
lista = [x for x in lista if x % 2 == 0]  # Utilizando uma list comprehension para criar uma nova lista sem os números ímpares

# Exibindo a lista após a remoção dos ímpares
print("Lista após remover os números ímpares:", lista)
