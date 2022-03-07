import requests
# import pandas as pd
from datetime import datetime
import time
import json
while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(requisicao.text)

    print('### COTACAO ###', datetime.date.now())
    print('Dólar: ', cotacao['valores']['USD']['valor'])
    print('EUR: ', cotacao['valores']['EUR']['valor'])
    print('BTC: ', cotacao['valores']['BTC']['valor'])
    time.sleep(2)