n1 = int(input('\033[1;31mDigite um número: \033[m'))
n2 = int(input('\033[1;32mDigite outro: \033[m'))
s = n1+n2
print('\033[33mA soma entre {} e {} vale {}\033[m'.format(n1, n2, s))