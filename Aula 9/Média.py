#Crie um programa em linguagem Python que leia 4 números,
#calcule e mostre a média aritmética dos valores lidos.

soma = 0
for i in range (4):
    numero = float(input('Digite o {}º número: '.format (i+1)))
    soma+= numero
    
media = soma/4
print('A média dos números é: ', media)