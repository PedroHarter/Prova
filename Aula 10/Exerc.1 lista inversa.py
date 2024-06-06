#Elabore um script em linguagem Python que leia de 10 números
#reais, inserindo-os numa lista e ao final, mostre-os na ordem inversa

numeros = []

for i in range(10):
    numero = float(input(f'Digite o {i+1}º número real: '))
    numeros.append(numero)
    
print('Números na ordem inversa:')
for num in reversed(numeros):
    print(num)