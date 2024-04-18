dinheiro = float(input('Digite quanto dinheiro você pretende gastar com gasolina: '))

litros = dinheiro / 4.95

quilometros = litros * 20

print('Com R$ %.2f, você pode comprar %.2f litros de gasolina.' %(dinheiro, litros))
print('Com essa quantidade de gasolina, o carro pode rodar %.2f quilômetros.' %quilometros)