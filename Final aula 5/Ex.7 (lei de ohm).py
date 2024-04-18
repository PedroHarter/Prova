tensao = float(input('Digite o valor da tensão (V) em Volts: '))
corrente = float(input('Digite o valor da corrente (i) em Amperes: '))
resistencia = float(input('Digite o valor da resistência (R) em Ohms: '))

tensao_esperada = corrente * resistencia

if tensao == tensao_esperada:
    print('O componente obedece a lei de Ohm.')
else:
    print('O componente não obedece a lei de Ohm.')