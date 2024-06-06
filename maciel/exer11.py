# Função para retornar uma lista com todos os valores entre x e y (inclusive)
def valores_entre(x, y):
    return list(range(x, y + 1))

# Testando a função
x = 2
y = 6
resultado = valores_entre(x, y)
print(f"Para x = {x}, y = {y}, resultado = {resultado}")
