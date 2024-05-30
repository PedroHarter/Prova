opcao = 0

while (opcao!=5):
    print('Digite a opção desejada')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    opcao=int(input('Escolha: '))
    if (opcao>=1 and opcao<=4):
        num1 = int(input('Digite n1: '))
        num2 = int(input('Digite n2: '))
        if opcao==1:
            res=num1+num2
        elif opcao == 2:
            res=num1-num2
        elif opcao ==3:
            res=num1*num2
        elif opcao == 4:
            res=num1/num2
        print('O resultado é: ',res)
    elif (opcao>5):
        print('Opção inválida')