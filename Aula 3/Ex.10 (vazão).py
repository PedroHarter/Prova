import math

diametro = float(input('Digite o diâmetro interno do tubo (em metros): '))
velocidade_fluxo = float(input('Digite a velocidade do fluxo (em segundos): '))

vazao = math.pi * (diametro / 2)**2 * velocidade_fluxo

print('A vazão do fluido é: %.2f metros cúbicos por segundos' %vazao)
