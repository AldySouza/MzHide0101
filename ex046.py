print('Contagem regressiva')
for c in range(10, -1, -1):
    print(c)
    from time import sleep
    sleep(1)
from emoji import emojize

print(emojize('Fim!:fireworks:', use_aliases=True))
