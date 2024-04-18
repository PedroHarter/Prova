nota1 = float(input('Digite a nota da primeira avaliação: '))
nota2 = float(input('Digite a nota da segunda avaliação: '))
nota3 = float(input('Digite a nota da terceira avaliação: '))

media = (nota1 + nota2 + nota3) / 3

print('A média das notas é: %.2f' %media)

if media >= 7.0:
    print('Sua média é alta!')
elif media >= 5.0:
    print('Sua média é razoável.')
else:
    print('Sua média é baixa')
    