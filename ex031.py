distancia = float(input('Qual a distância da sua viagem em Km? '))
if distancia <= 200:
    print('Sua viagem irá custar R$ {}.'.format(distancia*0.5))
else:
    print('Sua viagem irá custar R$ {}'.format(distancia*0.45))
