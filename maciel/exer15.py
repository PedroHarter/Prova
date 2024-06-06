# Lendo a temperatura média de cada mês do ano
temperaturas = []
for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média do mês {mes}: "))
    temperaturas.append(temperatura)

# Calculando a média anual das temperaturas
media_anual = sum(temperaturas) / len(temperaturas)

# Mostrando as temperaturas acima da média anual e em quais meses elas ocorreram
print("Temperaturas acima da média anual:")
for mes, temperatura in enumerate(temperaturas, start=1):
    if temperatura > media_anual:
        print(f"{mes} - {temperatura}°C")
