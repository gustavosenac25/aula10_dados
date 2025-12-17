# Atividade  01
# VsCode - GitHub

def soma_numeros(a , b):
    soma = a + b
    return soma


for num in range(3):
    try:
        numeroa = float(input('Informe o primeiro número: '))
        numerob = float(input('Informe o segundo número: '))
        resultado = soma_numeros(numeroa, numerob)
        print(f'A soma de {numeroa} e {numerob} é: {resultado}')
    except ValueError:
        print('Digite apenas números')
    except TypeError:
        print('Digite apenas números')