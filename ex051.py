primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
dec = primeiro + (10 - 1) * razão #formula do enézimo termo de uma pa
for c in range(primeiro, dec + razão, razão):
    print('{} '.format(c), end='--> ')
print('Acabou!')
