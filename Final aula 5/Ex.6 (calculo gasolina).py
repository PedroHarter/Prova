preco_alcool = 4.98
preco_gasolina = 5.57

litros_vendidos = float(input('Digite o número de litros abastecidos: '))
tipo_combustivel = input('Digite o tipo de combustível (A para Álcool ou G para Gasolina): ')

#Calcular valor a ser pago pelo cliente
if tipo_combustivel == 'A':
    if litros_vendidos <= 20:
        valor_pagar = litros_vendidos * preco_alcool * 0.98 #Desconto de 2% até 20 litros
        print('O valor que você irá pagar é R$%.2f' %valor_pagar)
    else:
        valor_pagar = litros_vendidos * preco_alcool * 0.95 #Desconto de 5% acima de 20 litros
        print('O valor que você irá pagar é R$%.2f' %valor_pagar)

elif tipo_combustivel == 'G':
    if litros_vendidos <= 20:
        valor_pagar = litros_vendidos * preco_gasolina * 0.96   #Desconto de 4% até 20 litros
        print('O valor que você irá pagar é R$%.2f' %valor_pagar)
    else:
        valor_pagar = litros_vendidos * preco_gasolina * 0.92   #Desconto de 8% acima de 20 litros
        print('O valor que você irá pagar é R$%.2f' %valor_pagar)
else:
    print('Tipo de combustível inválido. Use A para Álcool ou G para Gasolina.')