# def calcula_imc(p,a):
#     imc = p / (a ** 2)
#     return imc

# peso = float(input('Informe o peso: '))
# altura = float(input('Infome a altura: '))

# imc_calculado = calcula_imc(peso , altura)
# print(imc_calculado)

# if imc_calculado < 17:
#     print('Muito abaixo do peso')
# elif imc_calculado <= 18.4:
#     print('Abaixo do peso')
# elif imc_calculado <= 29.9:
#     print('Peso normal')
# elif imc_calculado <= 34.9:
#     print('Obesidade grau I')
# elif imc_calculado <= 40:
#     print('Obesidade grau II')
# else:
#     print('Obesidade grau III')


# def calcula_atingimento(v , m):
#     r = v / m * 100
#     return r

# for nun in range(1,4):
#     try:
#         venda = float(input('Informe o valor da venda: '))
#         meta = float(input ('Informe a meta do vendor: '))
#         resultado = calcula_atingimento(venda , meta)
#         print(f'Resultado: {resultado}%')
#     except ValueError:
#         print('\nErro! Digite apenas números')
#     except ZeroDivisionError:
#         print('\nErro! Digite um valor diferente de zero')

#ou

# for nun in range(1,4):
#     try:
#         venda = float(input('Informe o valor da venda: '))
#         meta = float(input ('Informe a meta do vendor: '))
#         resultado = calcula_atingimento(venda , meta)
#     except ValueError:
#         print('\nErro! Digite apenas números')
#     except ZeroDivisionError:
#         print('\nErro! Digite um valor diferente de zero')
#         exit()
#     except KeyboardInterrupt:
#         print('\nOperação finalizada pelo usuário')
#     else:
#         print(f'Resultado: {resultado}%')
#     finally:
#         print('Operação finalizada')
    