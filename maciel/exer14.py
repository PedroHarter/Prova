# Inicializando o dicionário vazio para armazenar os dados das pessoas
pessoas = []

# Lendo nome, altura e peso de 15 pessoas e armazenando no dicionário
for i in range(15):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
    peso = float(input(f"Digite o peso da pessoa {i + 1} (em kg): "))
    pessoas.append({"nome": nome, "altura": altura, "peso": peso})

# Encontrando a menor altura do grupo
menor_altura = min(pessoas, key=lambda x: x["altura"])["altura"]

# Calculando o peso médio do grupo
peso_total = sum(pessoa["peso"] for pessoa in pessoas)
peso_medio = peso_total / len(pessoas)

# Ordenando os nomes das pessoas em ordem alfabética
nomes_ordenados = sorted([pessoa["nome"] for pessoa in pessoas])

# Mostrando os resultados
print(f"A menor altura do grupo é: {menor_altura} metros")
print(f"O peso médio do grupo é: {peso_medio:.2f} kg")
print("Lista dos nomes das pessoas em ordem alfabética:")
for nome in nomes_ordenados:
    print(nome)
