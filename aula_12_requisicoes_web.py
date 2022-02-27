import requests

try:
    requisicao = requests.get('https://solyd.com.br')
except:
    print('Requisição deu erro!');

print(requisicao) 