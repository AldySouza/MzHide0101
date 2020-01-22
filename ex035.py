print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
a = float(input('Primeiro seguimento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
#if (a+b) > c and (a+c) > b and (b+c) > a:
    #print('Os segmentos acima PODEM FORMAR um triângulo!')
if (a+b) > c and (a+c) > b and (b+c) > a and a == b == c:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    print('Este triângulo é um triângulo EQUILÁTERO.')
elif (a+b) > c and (a+c) > b and (b+c) > a and (a == b or a == c or b == c):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    print('Este triângulo é um triângulo ISÓSCELES.')
elif (a+b) > c and (a+c) > b and (b+c) > a and (a != b != c):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    print('Este triângulo é um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
