"""
exercício: faça um programa que leia a quantidade de pessoas que serao convidados
para uma festa.
após isso o programa irá perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá imprimir todos os nomes da lista
"""


convidados = input('Coloque o número de convidado: ')
lista_de_convidados = []

i = 1
while i <= int(convidados):
    nome_do_convidado = input('Coloque o nome do convidado: #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidado)
    i += 1

print('\nNÚMERO DE CONVIDADOS: ', convidados)
print('\nLISTA DE CONVIDADOS: ')

for convidado in lista_de_convidados:
    print('convidado: ', convidado)


# lista_convidados = ['carlos', 'andre', 'caio', 'fabio']

# while lista_convidados >= 3:
#     print('convidado número: ', lista_convidados)
#     lista_convidados = lista_convidados + 1

# print(lista_convidados)



