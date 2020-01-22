salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.1)
print('Quem ganha R${} passa a ganhar R${} agora.'.format(salario, novo))

