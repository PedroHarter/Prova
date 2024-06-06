x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

valores = []

if x < y:
    valores = list (range(x,y+1))
    print(f'Para x = {x} e y = {y}, resultado = {valores}')
else:
    print('Erro: x deve ser menor que y.')