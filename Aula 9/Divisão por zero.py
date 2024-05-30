a = int(input('Digite um numero QUALQUER: '))
b = int(input('Digite um numero DIFERENTE de 0 (zero): '))

try:
    print (a/b)
except ZeroDivisionError:
    print ('Divisão por zero - inválida!')
