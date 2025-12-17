lst_vendas = [] #Sem nada dentro da chave significa que é infinita
resposta = 's'
venda = 1 #para que comece no item 1
tentativa = 1

#enquanto as respostas do usúario for sim, continua a repetição

# while resposta != 'n': #enquanto a resposta for diferente de n, ou seja, for sim para a pergunta la em baixo: Quer continuar?
#     try:
#         valor = float(input(f'Informe o valor da {venda}ª venda: '))
#     except ValueError:
#         print('Informe apenas números')
#     except KeyboardInterrupt:
#         print('Operação encerrada pelo usuário')
#         break
#     else:
#         lst_vendas.append(valor) #adicionar o valor na lista
#         resposta = input('Quer continuar? [s/n]') [0].lower() #caso o unuario digite SIM ou NAO, esse codigo usa somente a primeira letra e torna tudo em minisculo
#         venda += 1 #venda passa a signicar 2... depois 3... depois 4...
#     finally:
#         print(f'Tentativa {tentativa} \n')
#         tentativa += 1

# print(f'Vendas registradas: {lst_vendas}')