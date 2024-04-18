a = int(input('Digite um número: '))
b = int(input('Digite um número diferente de zero: '))

try:
    print (a/b)
except ZeroDivisionError:
    print ('Divisão por zero inválida')