funcionarios = {
    1: 'João',
    2: 'Maria',
    3: 'Pedro',
    4: 'Ana'
}

print ('Funcionários:')
for indice, nome in funcionarios.items():
    print(f'{indice}:{nome}')
    
num_funcionarios = int(input('\nDigite o número do funcionário a ser demitido:'))

if num_funcionarios in funcionarios:
    funcionario_demitido = funcionarios.pop(num_funcionarios)
    print(f'\nFuncionário {funcionario_demitido} demitido com sucesso!')
else:
    print('\nNúmero de funcionário inválido.')

print('\nFuncionários restantes:')
for indice, nome in funcionarios.items():
    print(f'{indice}:{nome}')