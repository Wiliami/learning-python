#operadores: 
# igual: ==
# diferente: !=
# maior: > 
# menor: < 
# maior igual: >=
# menor igual: <=

# and: E
# or: OU


# var_verdade = True
# var_false = False

#print(var_verdade)

# if True:
#     print ("var_verdade é:", var_verdade)


# a =  30
# b = 20

# if a > b and 'abacaxi' == 'uva': 
#     print(a, 'é maior do que', b)
# else:
#     print('Não deu certo o if')

print('Opções:\n1 = Escreve João\n2 = Escreva Maria\n3 = Escreva Júlia')

opcao = input('Escolha uma opção: ')

if opcao == '1':
    print('João')
elif opcao == '2':
    print('Maria')
elif opcao == '3':
    print('Júlia')
else:
    print('Opção inválida!')