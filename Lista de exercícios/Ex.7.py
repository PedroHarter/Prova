#Desenvolver um script em linguagem Python que leia a velocidade máxima permitida em uma avenida e a 
#velocidade com que o motorista estava dirigindo por ela. Em seguida calcule o valor da multa que uma pessoa
#receberá, sabendo que são pagos: a) R$ 85,13 se o motorista ultrapassar em até 10 km/h a velocidade permitida;
#b) R$ 127,69 se o motorista ultrapassar de 11 a 30 km/h a velocidade permitida; c) R$ 574,62 se estiver acima de
#31 km/h da velocidade permitida. Informe também os pontos que serão inseridos na carteira e o tipo de multa que
#será aplicado de acordo com a relação a seguir: Leve, Media e Gravíssima com 3, 5 e 7 pontos, respectivamente.
#Caso o motorista passe dentro da velocidade permitida, exibir “Vel. Normal”.
#8)

velocidade_permitida = float(input('Informe a velocidade máxima permitida (em km/h): '))
velocidade_motorista = float(input('Informe a velocidade do motorista (em km/h): '))

diferenca_velocidade = velocidade_motorista - velocidade_permitida

if diferenca_velocidade <= 10:
    multa = 85.13
    tipo_multa = 'Leve'
    pontos = 3
elif diferenca_velocidade <= 30:
    multa = 127.69
    tipo_multa = 'Média'
    pontos = 5
else:
    multa = 574.62
    tipo_multa = 'Gravíssima'
    pontos = 7

if diferenca_velocidade <= 0:
    print('Vel. Normal')
else:
    print (f'Multa a ser paga: {multa:.2f}')
    print (f'Tipo de multa: {tipo_multa}')
    print (f'Pontos na carteira: {pontos}')