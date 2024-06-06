# Crie um script em linguagem Python que leia dois vetores com 5elementos cada.
# Gere um terceiro vetor de 10 elementos, cujosvalores deverão ser compostos pelos elementos intercalados dos doisoutros vetores.
# Exibir na tela todos os vetores em linhas separadas.

vetor1 = []
vetor2 = []

print('Digite os elementos do primeiro vetor: ')
for i in range(5):
    elemento = input(f'Elemento {i+1}: ')
    vetor1.append(elemento)
    
print('Digite os elementos do segundo vetor: ')
for i in range(5):
    elemento = input(f'Elemento {i+1}: ')
    vetor2.append(elemento)
    
vetor_intercalado = []
for i in range(5):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])
    
print('Vetor 1:')
for elemento in vetor1:
    print(elemento, end= '')
print()

print('Vetor 2:')
for elemento in vetor2:
    print(elemento, end='')
print()

print('Vetor intercalado:')
for elemento in vetor_intercalado:
    print(elemento, end= '')