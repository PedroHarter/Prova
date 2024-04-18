letra = input('Digite uma letra: ')

if letra.lower() in 'aeiou':
    print('Essa letra é uma vogal.')
elif letra.isalpha():
    print('Essa letra é uma consoante.')
else:
    print('O caractere digitado não é uma letra.')