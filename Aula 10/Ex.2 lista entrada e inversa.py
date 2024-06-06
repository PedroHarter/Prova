#Desenvolva um script em linguagem Python com uma lista vazia. Emseguida, leia e insira 5 valores inteiros na lista.
# Ao final mostre na tela, osvalores contidos na lista. Ordem de entrada e inversa.

lista = []

for i in range(5):
    valor = int(input('Digite um valor inteiro: '))
    lista.append(valor)

print('Valores na ordem de entrada:')
for item in lista:
    print(item)
print('Valores na ordem inversa:')
for item in reversed(lista):
    print(item)