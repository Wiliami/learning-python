import requests
import json


requisicao = ''
cidade = input('Escreva sua cidade: ')
requisicao = requests.get('api.openweathermap.org/data/2.5/weather?q='+cidade+'&app id=81af18b4bea490ff86824dc7e74c000b')
#print(requisicao.text)

tempo = json.loads(requisicao.text)
print(tempo['weather'])
