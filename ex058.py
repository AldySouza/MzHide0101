from random import randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)

print('')
num = int(input('Qual é o seu palpite? ')) #Jogador tenta adivinhar...
pc = randint(0, 10)
tentativas = 1

while num != pc:
    tentativas += 1
    print('Tentativa {}'.format(tentativas))
    num = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar...
    print('PROCESSANDO...')
    from time import sleep
    sleep(1)
    if num == pc:
        print('PARABÉNS! Você conseguiu me vencer! Depois de {} tentativas.'.format(tentativas))

    else:
        print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, num))
