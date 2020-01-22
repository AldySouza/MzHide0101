v = int(input('Velocidade em Km/h: '))
if v > 80:
    print('MULTADO. a multa vai custar R${}.'.format((v-80)*7))
else:
    print('Dentro do limite!')
