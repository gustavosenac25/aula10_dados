def calcula_imc(p,a):
    imc = p / (a ** 2)
    return imc

peso = float(input('Informe o peso: '))
altura = float(input('Infome a altura: '))

imc_calculado = calcula_imc(peso , altura)
print(imc_calculado)

if imc_calculado < 17:
    print('Muito abaixo do peso')
elif imc_calculado <= 18.4:
    print('Abaixo do peso')
elif imc_calculado <= 29.9:
    print('Peso normal')
elif imc_calculado <= 34.9:
    print('Obesidade grau I')
elif imc_calculado <= 40:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')
