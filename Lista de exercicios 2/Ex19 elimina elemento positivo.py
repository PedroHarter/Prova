#Leia um vetor com 20 número inteiros. Escreva os elementos do vetoreliminando elementos repetidos.

vetor = []
print('Digite 20 números inteiros: ')
for _ in range(20):
    numero = int(input())
    vetor.append(numero)
    
elementos_unicos = set(vetor)

print('Elementos do vetor sem repetição:')
for elemento in elementos_unicos:
    print(elemento)
