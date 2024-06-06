# Inicializando a lista para armazenar os números
numeros = []

# Loop para ler os números
while True:
    numero = int(input("Digite um número positivo (ou -1 para sair): "))
    if numero == -1:  # Se o número digitado for -1, o loop é interrompido
        break
    elif numero >= 0:  # Se o número for positivo, ele é adicionado à lista
        numeros.append(numero)
    else:  # Se o número for negativo, uma mensagem de erro é exibida
        print("Número inválido. Por favor, insira um número positivo.")

# Calculando a soma, média, menor e maior número
if numeros:
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    print(f"Soma: {soma}")
    print(f"Média: {media}")
    print(f"Menor número: {menor}")
    print(f"Maior número: {maior}")
else:
    print("Nenhum número positivo foi inserido.")
