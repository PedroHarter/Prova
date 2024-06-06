valor = 135.0

notas100 = int(valor / 100)
valor = valor % 100
print('Entregar', notas100, 'notas de 100')

notas50 = int(valor / 50)
valor = valor % 50
print('Entregar', notas50, 'notas de 50')

notas20 = int(valor / 20)
valor = valor % 20
print('Entregar', notas20, 'notas de 20')

notas10 = int(valor / 10)
valor = valor % 10
print('Entregar', notas10, 'notas de 10')

notas5 = int(valor / 5)
valor = valor % 5
print('Entregar', notas5, 'notas de 5')
