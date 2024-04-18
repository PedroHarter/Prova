#Elabore um script em linguagem Python que leia três números e mostre o maior deles.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    maior_numero = n1
elif n2 >=n1 and n2 >= n3:
    maior_numero = n2
else:
    maior_numero = n3
    
print('O maior número é:', maior_numero)
