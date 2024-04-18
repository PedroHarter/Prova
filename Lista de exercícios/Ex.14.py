#Criar um script em linguagem Python que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_por_hora = float(input('Digite o salário por hora: '))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))

salario_total = salario_por_hora * horas_trabalhadas

print('O total do seu salário no referido mês é: %.2f' %salario_total)