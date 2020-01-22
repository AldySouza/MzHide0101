from random import randint
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
pc = randint(0,5)
tentativas = 5
rodada = 1
while(rodada <= tentativas):
    print('Tentativa {} de {}'.format(rodada,tentativas))
    num = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar...
    print('PROCESSANDO...')
    from time import sleep
    sleep(2)
    if num == pc:
        print('PARABÉNS! Você conseguiu me vencer!')

    else:
        print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, num))
    rodada = rodada + 1
