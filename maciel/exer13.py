# Solicitando ao usuário inserir a descrição e preço de três produtos
produtos = {}
for i in range(3):
    descricao = input(f"Digite a descrição do produto {i + 1}: ")
    preco = float(input(f"Digite o preço do produto {i + 1}: "))
    produtos[descricao] = preco

# Encontrando o produto mais caro
produto_mais_caro = max(produtos, key=produtos.get)

# Mostrando na tela o nome do produto mais caro
print(f"O produto mais caro é: {produto_mais_caro}")
