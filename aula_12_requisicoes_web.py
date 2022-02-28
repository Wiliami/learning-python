import requests


texto = None
try:
    requisicao = requests.get('https://putsreq.com/XBBRHp2Yq3IP5KqLIFBp')
    texto = requisicao.text

except Exception as e: 
    print('Requisição deu erro!', e);

print(texto) 