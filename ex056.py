soma_idade = 0
media_idade = 0
maioridade_homem = 0
nome_maisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioridade_homem = idade
        nome_maisvelho = nome
    if sexo in 'Mm' and idade > maioridade_homem:
        maioridade_homem = idade
        nome_maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade_homem, nome_maisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))