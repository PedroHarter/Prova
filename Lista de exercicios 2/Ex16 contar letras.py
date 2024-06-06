#Elabore um script que crie um dicionário na qual cada chave seja umcaractere e seu valor seja o número de vezes que o caractere aparece na frase.Exemplo:
#"Digite uma frase para contar as letras:“ – eu sei
#Resposta {'e': 2, 'u': 1, ' ': 1, 's': 1, 'i': 1}

frase = input('Digite uma frase (exemplo Eu Sei):')
print('A quantidade de caracteres de sua frase é:', len(frase))
d = {}
lista = list(frase)
print(lista)
for letra in lista:
    d[letra] = lista.count(letra)
print(d)