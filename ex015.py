a = float(input('Quantos dias alugados? '))
r = float(input('Quantos Km rodados? '))
da = 60*a
kr = 0.15*r
print('O total a pagar é de R${:.2f}'.format(da+kr))
