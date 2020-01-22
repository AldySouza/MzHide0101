m = int(input('Digite um valor em metros: '))
c = m*(10**2)
mm = m*(10**3)
print('Seu valor em centímetros é {} e em milímetros é {}.'.format(c,mm))

m = int(input('Uma distância em metros: '))
print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(m, (m/(10**3)), (m/(10**2)), (m/10), (m*10), (m*(10**2)), (m*(10**3))))
