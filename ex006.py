n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n*(1/2)
print('O seu dobro vale {}, o triplo vale {} e sua raiz quadrada vale {}.'.format(d,t,r))

n = int(input('Digite um número: '))
print('Analizando o valor {}, o seu dobro vale {}, o seu triplo vale {} e sua raiz quadrada vale {}.'.format(n, (n*2), (n*3), (n**(1/2))))

n = int(input('Digite um número: '))
print('O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
