# Definindo o dicionário de produtos
produtos = {
    1: {"nome": "Produto 1", "preco_unitario": 10.5, "quantidade": 2},
    2: {"nome": "Produto 2", "preco_unitario": 20.3, "quantidade": 1},
    3: {"nome": "Produto 3", "preco_unitario": 15.75, "quantidade": 3}
}

# Calculando e imprimindo o subtotal de cada item
for codigo, produto in produtos.items():
    subtotal = produto["preco_unitario"] * produto["quantidade"]
    print(f"{produto['nome']}: Subtotal = R${subtotal:.2f}")

# Calculando e imprimindo o valor total da compra
total = sum(produto["preco_unitario"] * produto["quantidade"] for produto in produtos.values())
print(f"Valor total da compra: R${total:.2f}")
