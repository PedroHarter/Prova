d = {}

d['nome'] = input('Digite o nome: ')
d['idade'] = input('Digite a idade: ')
d['endereço'] = input('Digite o endereço: ')
d['telefone'] = input('Digite o telefone: ')

print('\nDados inseridos:')
for chave, valor in d.items():
    print(f'{chave}: {valor}')