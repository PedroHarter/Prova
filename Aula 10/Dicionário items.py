#O método items() de um dicionário retorna ambos, na forma de umalista de tuplas - cada tupla com um par chave-valor

D = {'arroz': 17.30, 'feijão': 12.50, 'carne': 23.90, 'alface':3.40}

print(D)

for alimento, preco in D.items():
    print(f'{alimento} = {preco:.2f}')