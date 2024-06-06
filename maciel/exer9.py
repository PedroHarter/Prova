# Criando um dicionário vazio
d = {}

# Solicitando os dados ao usuário
d['nome'] = input("Digite o nome: ")
d['idade'] = int(input("Digite a idade: "))
d['endereço'] = input("Digite o endereço: ")
d['telefone'] = input("Digite o telefone: ")

# Mostrando os dados inseridos
print("Dados inseridos:")
for chave, valor in d.items():
    print(f"{chave.capitalize()}: {valor}")
