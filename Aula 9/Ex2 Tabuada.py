N = int(input('Digite um número da tabuada desejada: '))

print('Tabuada de ',N)

for i in range(1,11) :
    resultado = N*i
    print(N, 'X', i, '=', resultado)