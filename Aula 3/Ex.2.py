deslocamento = float(input('Digite a variação de deslocamento: '))
tempo = float(input('Digite a variação do tempo percorrido: '))

velocidade = deslocamento / tempo

print('Variação do deslocamento: ',deslocamento, 'metros')
print('Variação do tempo percorrido:', tempo, 'segundos')

print('\nVelocidade do corpo: %.2f' %velocidade, 'm/s')