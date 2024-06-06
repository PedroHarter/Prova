#Desenvolver um script em linguagem Python que leia nome, altura e pesode 15 pessoas. Este programa deverá armazená-los em um Dicionário, bemcomo calcular e mostrar:
#a. A menor altura do grupo;
#b. O peso médio do grupo;
#c. Uma lista dos nomes das pessoas em ordem alfabética.

import statistics

pessoas = {}

for i in range(15):
    nome = input(f'Digite o nome da {i+1}º pessoa: ')
    altura = float(input(f'Digite a altura da {i+1}º pessoa (em metros): '))
    peso = float(input(f'Digite o peso da {i+1}º pessoa (em kg): '))
    pessoas[nome] = {'altura' : altura, 'peso': peso}
    
    menor_altura = min(pessoa['altura'] for pessoa in pessoas.values())
    
    peso_medio = statistics.mean(pessoa['peso'] for pessoa in pessoas.values())
    
    nomes_ordenados = sorted(pessoas.keys())
    
    print(f'A menor altura do grupo é: {menor_altura:.2f} metros.')
    print(f'O peso médio do grupo é: {peso_medio:.2f} kg')
    print('Lista dos nomes das pessoas em ordem alfabética:')
    for nome in nomes_ordenados:
        print(nome)