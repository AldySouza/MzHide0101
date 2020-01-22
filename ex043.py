altura = float(input('Digite sua altura em METROS: '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC é igual a {:.2f}. Você está abaixo do peso recomendado.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é igual a {:.2f}. Você está na faixa de peso ideal.'.format(imc))
elif 25 <= imc <= 30:
    print('Seu IMC é igual a {:.2f}. Você está com sobrepeso.'.format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é igual a {:.2f}. Você está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é igual a {:.2f}. Você está com obesidade móbida.'.format(imc))
