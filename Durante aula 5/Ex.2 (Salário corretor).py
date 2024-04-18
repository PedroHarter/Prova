nome_corretor = input('Digite o nome do corretor: ')
quantidade_imoveis_vendidos = int(input('Digite a quantidade de imóveis vendidos: '))
valor_total_vendas = float(input('Digite o valor total de suas vendas: '))

salario_base = 1500.00
comissao_por_imovel = 200.00
porcentagem_comissao_vendas = 0.05

comissao_vendas = comissao_por_imovel * quantidade_imoveis_vendidos + (porcentagem_comissao_vendas * valor_total_vendas)

salario_final = salario_base + comissao_vendas

print(f'O salário final do corretor {nome_corretor} é: R${salario_final:,.2f}')
