# Desenvolva um script em linguagem Python que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.

medias_alunos = []

for i in range(10):
    print(f'Informe as notas do aluno {i+1}: ')
    notas = []
    for j in range(4):
        nota = float(input(f'Nota {j+1}: '))
        notas.append(nota)
        
    media = sum(notas) / len(notas)
    medias_alunos.append(media)
    
alunos = sum(media >= 7 for media in medias_alunos)

print(f'\nNúmeros de alunos com média maior ou igual a 7: {alunos}')