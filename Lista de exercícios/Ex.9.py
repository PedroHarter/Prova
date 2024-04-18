#Desenvolva um script em linguagem Python que leia dois valores numéricos inteiros para duas variáveis e que
#troque o conteúdo dessas variáveis, visualizando o valor das mesmas antes e depois da troca.

valor1 = int(input('Digite o primeiro valor inteiro: '))
valor2 = int(input('Digite o segundo valor inteiro: '))

print('Valores antes da troca:')
print('Valor 1:', valor1)
print('Valor 2:', valor2)

aux = valor1
valor1 = valor2
valor2 = aux

print('\nValores depois da troca:')
print('Valor 1:', valor1)
print('Valor 2:', valor2)