#Em um script Python com duas listas de três elementos com númerosinteiros, crie uma nova lista onde cada elemento é a soma dos elementos demesma posição nas duas primeiras listas.
#Exemplo: Lista1 = [1, 4, 6] Lista2 = [2, 4, 3] Lista_resultante = [3, 8, 9]

lista1 = []
lista2 = []

print('Insira os elementos da primeira lista:')
for i in range(3):
    elemento = int(input(f'Digite o elemento {i+1}: '))
    lista1.append(elemento)
    
print('\nInsira os elementos da segunda lista:')
for i in range(3):
    elemento = int(input(f'Digite o elemento {i+1}: '))
    lista2.append(elemento)
    
soma_elementos = []

for i in range(len(lista1)):
    soma_elementos.append(lista1[i] + lista2[i])
    
print('\nNova lista com a soma dos elementos de mesma posição nas duas listas:',soma_elementos)