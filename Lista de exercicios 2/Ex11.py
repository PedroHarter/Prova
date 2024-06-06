#Elabore um script em linguagem Python que, dados dois inteiros x e y,retorna uma lista com todos os valores entre x e y (inclusive), considerando x <y.
#Exemplos x = 2, y = 6, resultado = [2, 3, 4, 5, 6]

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

valores = []

if x < y:
    valores = list (range(x,y+1))
    print(f'Para x = {x} e y = {y}, resultado = {valores}')
else:
    print('Erro: x deve ser menor que y.')