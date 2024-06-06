# Lendo as duas listas de seis elementos
lista1 = [int(input(f"Digite o elemento {i + 1} da lista 1: ")) for i in range(6)]
lista2 = [int(input(f"Digite o elemento {i + 1} da lista 2: ")) for i in range(6)]

# Criando a nova lista com a soma dos elementos de mesma posição nas duas listas
lista_resultante = [lista1[i] + lista2[i] for i in range(6)]

# Exibindo a lista resultante
print("Lista resultante:", lista_resultante)
