#Gerenciador de pagamentos

preço = float(input('Preço do produto: R$'))
print('''Condições de pagamento:
[ 1 ] À vista (Dinheiro/Cheque): 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: Preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opção = int(input('Sua opção: '))
o1 = preço - (preço * 0.1)
o2 = preço - (preço * 0.05)
o3 = preço
o4 = preço + (preço * 0.2)
if opção == 1:
    print('O preço do produto com 10% de desconto ficará R${}'.format(o1))
elif opção == 2:
    print('O preço do produto com 5% de desconto ficará R${}'.format(o2))
elif opção == 3:
    print('O preço do produdo será R${}'.format(o3))
elif opção == 4:
    print('O preço do produto com 20% de juros ficará R${}'.format(o4))
    