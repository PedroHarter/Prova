produtos = {}

for i in range(3):
    nome_produto = input(f'Insira o nome do produto {i+1}: ')
    preco_produto = float(input(f'Insira o preço do produto {i+1}: '))
    produtos [nome_produto] = preco_produto
    
print('\nProdutos e preços inseridos:')
for produto, preco in produtos.items():
    print(f'Produto: {produto}, Preço: R${preco:.2f}')