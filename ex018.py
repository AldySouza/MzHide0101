import math
an = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O ângulo de {} tem \no SENO de {:.2f} \no COSSENO de {:.2f} \ne a TANGENTE de {:.2f}'.format(an, seno, cos, tg))
