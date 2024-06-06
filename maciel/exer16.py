# Solicitando ao usuário inserir uma frase
frase = input("Digite uma frase para contar as letras: ")

# Criando um dicionário para contar as letras
contagem_letras = {}
for letra in frase:
    if letra in contagem_letras:
        contagem_letras[letra] += 1
    else:
        contagem_letras[letra] = 1

# Mostrando o resultado
print("Resposta:", contagem_letras)
