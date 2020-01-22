print('\033[30m-=-\033[m'*20)
print('\033[1;34mConfederação Nacional de Natação\033[m')
print('\033[30m-=-\033[m'*20)
ano = int(input('Digite o ano de nascimento: '))
idade = 2020 - ano
if idade <= 9:
    print('Você tem {} anos. Sua categoria é MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('Você tem {} anos. Sua categoria é INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('Você tem {} anos. Sua categoria é JUNIOR.'.format(idade))
elif idade == 20:
    print('Você tem 20 anos. Sua categoria é SÊNIOR.')
elif idade > 20:
    print('Você tem {} anos. Sua categoria é MASTER.'.format(idade))
