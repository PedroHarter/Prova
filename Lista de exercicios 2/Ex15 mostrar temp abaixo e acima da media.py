#Elabore um código em Python que leia a temperatura média de cada mêsdo ano e guarde em uma lista. 
# Com isso, efetue a média anual dastemperaturas e mostre todas que estão acima da média anual e em que mêselas ocorreram (Ex.: 1 – Janeiro, 2 – Fevereiro, etc).

temperaturas_mensais = {}

nomes_meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

for i in range(12):
    temp = float(input(f'Digite a temperatura média para o mês {nomes_meses[i]}:'))
    temperaturas_mensais.append(temp)
    
media_anual = sum(temperaturas_mensais)   / 12
print(f'\nA média anual das temperaturas acima da média anual:')
for i in range(12):
    if temperaturas_mensais[i] > media_anual:
        print(f'{i+1} - {nomes_meses[i]}: {temperaturas_mensais[i]:.2f}ºC')