# Solicitando o tamanho da turma
n = int(input("Tamanho da turma: "))

# Lendo as notas da prova 1
print("P1:", end=" ")
notas_p1 = [float(x) for x in input().split()]

# Lendo as notas da prova 2
print("P2:", end=" ")
notas_p2 = [float(x) for x in input().split()]

# Calculando as médias das provas
media_p1 = sum(notas_p1) / n
media_p2 = sum(notas_p2) / n

# Imprimindo as médias
print(f"Média da turma na prova 1: {media_p1:.2f}")
print(f"Média da turma na prova 2: {media_p2:.2f}")

# Comparando as médias para determinar qual é melhor
if media_p1 > media_p2:
    print("A turma obteve a melhor média na prova 1.")
elif media_p1 < media_p2:
    print("A turma obteve a melhor média na prova 2.")
else:
    print("A turma obteve a mesma média nas duas provas.")
