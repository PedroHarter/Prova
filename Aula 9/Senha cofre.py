#Desenvolva um programa que o usuário necessita digitar a senha de um cofre, esta senha é numérica (987654), 
# enquanto os valores digitais não forem corretos, o programa deverá 
# pedir novamente informando que o valor está incorreto, assim que estiver correto, informar, cofre aberto.

senha_correta = 987654

while True: 
    senha = int(input('Digite a senha: '))
    if senha == senha_correta:
        print('Senha correta.')
        break
    else:
        print('Senha incorreta. Tente novamente.')