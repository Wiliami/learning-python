## mini banco de dados
movies = [
    'A era do gelo',
    'Nárnia',
    'Homem Aranha', 
    'Deus não está morto', 
    'A era do gelo', 
    'Senhor dos Anéis', 
    'Um amor para recordar', 
    'The Batman', 
    'Branca de Neve',
    'Sonho de Natal'
]

pagina = open('movies.html', 'w')
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <title>Lista de filmes com python</title>
    </head>
    <body>
        <h1>Lista de filmes</h1>
""")
for movie in movies:
    pagina.write('<li href="/">%s</li>\n' % movie)
pagina.write("""
    </body>
</html>
""")
pagina.close();