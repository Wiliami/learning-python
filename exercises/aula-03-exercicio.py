"""
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do exército.
Para entrar no exército é preciso ter mais de 18 anos
 pesar mais ou igual 60 kilos
e medir mais ou ighual 1,70 metros
"""

welcome = 'Seja bem-vindo(a) ao exército!'
print(welcome)

idade = int(input('Qual a sua idade: '))
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))



if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Parabéns, voce está apto para servir ao Exército!')
else :
    print('Infelizmente voce não passou no teste!')