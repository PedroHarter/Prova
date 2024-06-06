votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_candidato_4 = 0
votos_nulos = 0
votos_em_branco = 0

while True:
    voto = int(input('Digite o código do candidato (ou 0 para encerrar): '))

    if voto == 0:
        break
    elif voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3: 
        votos_candidato_3 += 1
    elif voto == 4:
        votos_candidato_4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_em_branco += 1
    else:
        print('Código de voto inválido. Tente novamente.')
        
    print ('Total de votos para o candidato 1:', votos_candidato_1)
    print ('Total de votos para o candidato 2:', votos_candidato_2)
    print ('Total de votos para o candidato 3:', votos_candidato_3)
    print ('Total de votos para o candidato 4:', votos_candidato_4)
    print ('Total de votos nulos:', votos_nulos)
    print ('Total de votos em branco:', votos_em_branco)
    