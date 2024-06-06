# Lendo a primeira lista
lista1 = []
for i in range(5):
    elemento = int(input(f"Digite o elemento {i + 1} da primeira lista: "))
    lista1.append(elemento)

# Lendo a segunda lista
lista2 = []
for i in range(5):
    elemento = int(input(f"Digite o elemento {i + 1} da segunda lista: "))
    lista2.append(elemento)

# Gerando a terceira lista intercalada
lista3 = []
for i in range(5):
    lista3.append(lista1[i])  # Adicionando o elemento da primeira lista à lista intercalada
    lista3.append(lista2[i])  # Adicionando o elemento da segunda lista à lista intercalada

# Exibindo as listas
print("Primeira lista:", lista1)
print("Segunda lista:", lista2)
print("Terceira lista (intercalada):", lista3)
