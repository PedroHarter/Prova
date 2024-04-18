torque_aplicado = float(input('Digite o valor do torque aplicado (em Nm): '))
torque_recomendado = float(input('Digite o valor do torque de aperto recomendado (em Nm): '))

faixa_tolerancia_superior = torque_recomendado * 1.10
faixa_tolerancia_inferior = torque_recomendado * 0.9

if torque_aplicado >= faixa_tolerancia_inferior and torque_aplicado <= faixa_tolerancia_superior:
    print('O parafuso está apertado corretamente.')
else:
    print('O parafuso não está apertado corretamente.')