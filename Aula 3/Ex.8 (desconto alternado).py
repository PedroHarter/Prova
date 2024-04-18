preco_original = float(input('Digite o preço original do produto: '))
percentual_desconto = float(input('Digite o desconto a ser concedido: '))

desconto = (percentual_desconto / 100) * preco_original

preco_com_desconto = preco_original - desconto

print('Preço original do produto: R$ %.2f' %preco_original)

print('Valor do desconto: R$ %.2f' %desconto)

print('Valor do produto com desconto: R$ %.2f' %preco_com_desconto)