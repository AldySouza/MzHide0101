l = float(input('Largura em metros: '))
al = float(input('Altura em metros: '))
ar = l*al
t = ar/2
print('A largura da sua parede mede {}m, a altura mede {}m, a área vale {:.2f}m². A quantidade de tinta necessária é igual a {:.2f} litros.'.format(l,al,ar,t))
