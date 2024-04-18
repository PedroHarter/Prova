#Fazer um script em linguagem Python que solicita um número decimal e imprime o correspondente em hexa,
#binário e octal.

numero_decimal = int(input('Digite um número decimal: '))

numero_hexadecimal = hex(numero_decimal)
numero_binario = bin(numero_decimal)
numero_octal = oct(numero_decimal)

print('Número decimal:', numero_decimal)
print('Número hexadecimal:', numero_hexadecimal)
print('Número binário:', numero_binario)
print('Número octal:', numero_octal)