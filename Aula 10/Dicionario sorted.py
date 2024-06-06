D = {'arroz': 17.30, 'feijão': 12.50, 'carne': 23.90, 'alface':3.40}

print(D)

for alimento, preco in sorted(D.items()):
    print(f'{alimento} = {preco:.2f}')