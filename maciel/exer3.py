# Lista para armazenar as médias
medias = []

# Lendo as notas dos 10 alunos
for i in range(10):
    print(f"Notas do aluno {i + 1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j + 1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)  # Calculando a média das notas do aluno
    medias.append(media)  # Adicionando a média à lista de médias

# Contando o número de alunos com média maior ou igual a 7
alunos_acima_7 = sum(1 for media in medias if media >= 7)  # Utilizando uma expressão geradora para contar o número de alunos com média >= 7
print(f"Número de alunos com média maior ou igual a 7: {alunos_acima_7}")
