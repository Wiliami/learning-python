movies = ['A era do gelo', 'Nárnia', 'Homem Aranha', 'Deus não está morto', 'Peaky Blinders', 'A era do gelo', 'Senhor dos Anéis', 'Um amor para recordar', 'The Batman'] ## mini banco de dados

pagina = open('movies.html', 'w')
pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
    <head>
        <meta charset="utf-8">
        <title>Lista de filmes com python</title>
    </head>
    <body>
        <h1>Lista de filmes</h1>\n
""")
for movie in movies:
    pagina.write('<li href="/">%s</li>\n' % movie)
pagina.write("""
    </body>
</html>
""")
pagina.close()