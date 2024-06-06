#Em um script Python, crie uma lista vazia, que seja preenchida comnotas de 3 alunos. 
# Após a leitura das notas, mostrar a nota mais alta,
# anota mais baixa, a média geral de notas, além de ordenar a lista deforma crescente.

notas_alunos = []

for i in range(3):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas_alunos.append(nota)
    
nota_maxima = max(notas_alunos)
print('A nota mais alta é:',nota_maxima)

nota_minima = min(notas_alunos)
print('A nota mais baixa é:',nota_minima)

media_geral = sum(notas_alunos) / len(notas_alunos)
print('A média geral de notas é:',media_geral)

notas_alunos.sort(reverse=False)
print('Notas dos alunos em ordem crescente:',notas_alunos)