import re
import requests

requisicao = requisicao.get('https://deliveryapp.neemo.com.br/')

padrao = re.findall(r'[\w \.-]+@[ \w-]+ \.[ \w \.-]+', requisicao.text)


if padrao:
    print(padrao)
else:
    print("Padrão não encontrado!")

