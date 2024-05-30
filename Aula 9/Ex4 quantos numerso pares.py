i = 1
par = 0
while (i<=5):
    numero = int(input('Digite um número: '))
    if (numero%2 == 0):
        par = par +1
    i = i+1
print('A quantidade total de números par foi: ',par)