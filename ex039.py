ano = int(input('Digite o ano do seu nascimento: '))
idade = 2020 - ano
falta = 18 - idade
passou_idade = idade > 18
deveria_ter_alistado = idade - 18
ano_de_alistamento = ano + 18
if idade < 18:
    print('Quem nasceu em {} tem {} anos em 2020.\nFaltam {} anos para você se alistar.'.format(ano, idade, falta))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em 2020.\nVocê tem que se alistar IMEDIATAMENTE!'.format(ano, idade))
elif passou_idade:
    print('Quem nasceu em {} tem {} anos me 2020.\nVocê já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(ano, idade, deveria_ter_alistado, ano_de_alistamento))
