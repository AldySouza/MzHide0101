print('Comprando uma casa')
valor = float(input('Valor da casa em R$: '))
salario = float(input('Salário do comprador em R$: '))
anos = float(input('Em quantos anos você deseja financiar a casa? '))
parcela = valor / (anos*12)
if parcela <= (salario*0.3):
    print('A parcela do empréstimo no valor de {} dividido em {} anos custará {:.2f}.'.format(valor, anos, parcela))
else:
    print('O empréstimo foi negado pois a parcela excede o limite de 30% do salário.')
