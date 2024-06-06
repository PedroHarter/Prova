#Faça um programa que receba dois números inteiros e gere osnúmeros inteiros que estão no intervalo compreendido por eles.
#Mostre no final a soma dos números.

numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))

soma = 0

if numero1 < numero2:
    for i in range (numero1 + 1, numero2):
        print(i)
        soma += i
elif numero1 > numero2:
    for i in range (numero2 + 1, numero1):
        print(i)
        soma += i
else:
    print('Os números são iguais. Não há intervalos entre eles.')
print('A soma dos números no intervalo é:',soma)