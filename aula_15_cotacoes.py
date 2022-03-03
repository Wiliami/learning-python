import requets
import json

requisicao = requests.get('nome do site que tem as cotações das principais moedas')

# como o retorno da chamad get é um json, eu posso transformar em um objeto pyhton
cotacao = json.loads(requisicao.text) # vai retornar o objeto python formatado
print(cotacao)