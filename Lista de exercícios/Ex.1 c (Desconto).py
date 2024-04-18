valor_compra = float(input('Digite o valor da compra: '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

desconto = valor_compra * (percentual_desconto / 100)
valor_pago = valor_compra - desconto

print(f'O valor a ser pago após um desconto de {percentual_desconto:.2f}% é R${valor_pago:.2f}. ')