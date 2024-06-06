# Criando o dicionário com os funcionários
funcionarios = {
    1: {"nome": "João", "função": "Programador", "tempo_serviço": 2},
    2: {"nome": "Maria", "função": "Analista", "tempo_serviço": 4},
    3: {"nome": "Pedro", "função": "Programador", "tempo_serviço": 3},
    4: {"nome": "Ana", "função": "Gerente", "tempo_serviço": 5}
}

# Mostrando os funcionários
print("Funcionários:")
for codigo, funcionario in funcionarios.items():
    print(f"{codigo}: {funcionario['nome']} - {funcionario['função']} - {funcionario['tempo_serviço']} anos de serviço")

# Solicitando ao usuário o número do funcionário a ser demitido
num_demissao = int(input("Digite o número do funcionário a ser demitido: "))

# Verificando se o funcionário pode ser demitido
if funcionarios[num_demissao]["função"] == "Programador" and funcionarios[num_demissao]["tempo_serviço"] >= 3:
    print("Este funcionário não pode ser demitido.")
else:
    del funcionarios[num_demissao]
    print("Funcionário demitido com sucesso.")

# Mostrando os funcionários restantes
print("Funcionários restantes:")
for codigo, funcionario in funcionarios.items():
    print(f"{codigo}: {funcionario['nome']} - {funcionario['função']} - {funcionario['tempo_serviço']} anos de serviço")
