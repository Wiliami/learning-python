import requests
import json

req = None

def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=43924491&t=' + titulo)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro de conexão!')
        return None

def printar_detalhes(filme):
    print('Titulo:',filme['Title'])
    print('Ano:',filme['Year'])
    print('Diretor:',filme['Director'])
    print('Atores:',filme['Actors'])
    print('Nota:',filme['imdbRating'])
    print('')



sair = False
while not sair:
    op = input('Escreva um nome de filme ou SAIR para  fechar: ')

    if op == 'SAIR':
        sair =  True
    else:
        filme = requisicao(op)
        if filme['Response'] == False:
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)
 





#print(dicionario['title'])
