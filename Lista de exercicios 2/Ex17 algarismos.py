#Escreva um algoritmo que leia um número inteiro entre 100 e 999 eimprima na saída cada um dos algarismo que compõem o número.

while True:
    try:
        numero = int(input('Digite um numero inteiro entre 100 e 999: '))
        if 100<= numero <=999:
            break
        else:
            print('O numero deve estar entre 100 e 999.')
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')
        
centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

print(f'Centena: {centenas}')
print(f'Dezenas: {dezenas}')
print(f'Unidades: {unidades}')