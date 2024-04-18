frase = input('Digite uma frase: ')
palavra_antiga = input('Digite a palavra antiga: ')
palavra_nova = input('Digite a palavra nova: ')

frase_substituida = frase.replace(palavra_antiga, palavra_nova)

print('Frase original:',frase)
print('Frase com substituição:',frase_substituida)