i = 1
primo = 0
numero = int(input('Digite um número: '))
if (numero==1):
    print ('O numeral 1 não é primo')
else:
    while (1<=numero):
        if (numero%i == 0):
            primo=primo+1
        i=i+1
    if (primo==2):
        print ('Número primo')
    else:
        print('Não é primo')