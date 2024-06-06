#Escreva um programa que leia um número inteiro positivo n e em seguidaimprima n linhas chamado Triângulo de Floyd. Para n = 6, temos:
#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
#16 17 18 19 20 21

n = int(input('Digite um número inteiro positivo: '))

numero = 1
for linha in range(1, n+1):
    for coluna in range(1, linha+1):
        print(numero, end='')
        numero +=1
    print()